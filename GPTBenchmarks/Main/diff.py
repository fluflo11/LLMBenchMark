import cv2
import numpy as np
from Levenshtein import distance
import subprocess
from datetime import datetime
import sys

#Compiled tikz comparison
#Just two images comparison
#--------------------------------
def mse(imageA, imageB):
    if imageA.shape != imageB.shape:
        raise ValueError("the two tikz must have the same resolution")
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])
    return err

def comp_img(llm_img, expected_img):
    gradient1 = cv2.cvtColor(llm_img, cv2.COLOR_BGR2GRAY)
    gradient2 = cv2.cvtColor(expected_img, cv2.COLOR_BGR2GRAY)
    err = mse(gradient1, gradient2)
    return  err / 255.0

def img_acc(llm_img, expected_img):

    llm_img_content = cv2.imread(llm_img)
    if llm_img_content is None:
        raise ValueError("llm_img cant be loaded")
    
    expected_img_content = cv2.imread(expected_img)
    if expected_img_content is None:
        raise ValueError("expected_img cant be loaded")
    
    return comp_img(llm_img_content,expected_img_content)
    

"""Tikz Comparison

    tikz1 the file before llm modifications
    tikz2 the filer after llm modifications
    expected_add the expected added code
    expected_subb the expected removed code

"""
def comp_tikz(tikz1,tikz2,expected_add,expected_sub):

    res = subprocess.run(['diff', tikz1, tikz2], capture_output=True, text = True)
    res_str = res.stdout
    new_lines_list = []
    removed_lines_list = []

    for line in res_str.split('\n'):
        if line.startswith('>'):
            new_lines.append(line[2:])

    for line in res_str.split('\n'):
        if line.startswith('<'):
            removed_lines_list.append(line[2:])
    
    new_lines = '\n'.join(new_lines_list)
    removed_lines = '\n'.join(removed_lines_list)

    distance_new = distance(expected_add,new_lines)
    distance_old = distance(expected_sub,removed_lines)

    return (distance_new+distance_old)/2

"""
    Tikz Comparison
    
    tikz_llm the tikz modified by a llm
    tikz_perf the "perfect" tikz

"""
def comp_tikz_simple(tikz_llm,tikz_perf):
    
    with open(tikz_llm, 'r') as file:
        llm_content = file.read()
    with open(tikz_perf, 'r') as file:
        perf_content = file.read()
    
    llm_lines = []
    perf_lines = []

    for line in llm_content.split('\n'):
        llm_lines.append(line)
    for line in perf_content.split('\n'):
        perf_lines.append(line)

    not_present_count = sum(1 for line in llm_lines if line not in perf_lines)

    score = not_present_count / len(llm_lines)

    return score


        
    

"""
To implement : expected location
"""
def main(llm_tikz, perf_tikz, llm_img, perf_img):

    result = open("Results/results.txt", "w")
    """ Accuracy of the code modification """
    tikz_accuracy = comp_tikz_simple(llm_tikz,perf_tikz)

    """ Accuracy of the image modification """
    img_accuracy = img_acc(llm_img,perf_img)

    llm_accuracy = (tikz_accuracy + img_accuracy)/2

    date = (datetime.now()).strftime("%d/%m/%Y %H:%M:%S")
    
    text_to_write = ""
    text_to_write += "Date : " + date + "\n"
    text_to_write += "---------------------"
    text_to_write += "Tikz code accuracy : " + tikz_accuracy + "\n"
    text_to_write += "---------------------"
    text_to_write += "Image modification accuracy : " + img_accuracy + "\n"
    text_to_write += "---------------------"
    text_to_write += "Global accuracy : " + llm_accuracy
    
    result.write(text_to_write)
    

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Params to use diff.py : llm_tikz, perf_tikz, llm_img, perf_img")
    else :
        llm_tikz = sys.argv[1]
        perf_tikz = sys.argv[2]
        llm_img = sys.argv[3]
        perf_img = sys.argv[4]
        main(llm_tikz,perf_tikz,llm_img,perf_img)

