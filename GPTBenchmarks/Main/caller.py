import sys
import subprocess
import os
import time

def main(prompt_txt, tikz_tex, perf_tikz):

    print('\n' + 'Tikz compilation ------------' + '\n')

    script_dir = os.path.dirname(os.path.realpath(__file__))
    tikzcompiler_path = os.path.join(script_dir, 'tikzcompiler.py')
    if not os.path.isfile(tikzcompiler_path):
        print(f"error: {tikzcompiler_path} not found")
        return
    
    subprocess.run(['python3', tikzcompiler_path, tikz_tex])
    time.sleep(1)
#---------------------------------------------------------------
    print('\n' + 'Chatgptcaller ------------' + '\n')
    subprocess.run(['python3', 'chatgptcaller.py', tikz_tex, prompt_txt])
    time.sleep(1)
#---------------------------------------------------------------
    print('\n' + 'Tikz compilation ------------' + '\n')

    
    subprocess.run(['python3', tikzcompiler_path, '../Ressources/Tikz/tikz_res.tex'])
    subprocess.run(['python3', tikzcompiler_path, '../Ressources/Tikz/onlydog_modified.tex'])
    time.sleep(1)

#---------------------------------------------------------------
    print('\n' + 'Diff ------------' + '\n')
    perfect_img = perf_tikz.replace(".tex",".jpg")
    subprocess.run(['python3', 'diff.py',
                    '../Ressources/Tikz/tikz_res.tex',
                    perf_tikz,
                    '../Ressources/Tikz/tikz_res.jpg',
                    perfect_img])
    


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Params to use the script: prompt_txt, tikz_tex, perf_img, perf_tikz")
    else:
        prompt_txt = sys.argv[1]
        tikz_tex = sys.argv[2]
        perf_tikz = sys.argv[3]
        main(prompt_txt, tikz_tex, perf_tikz)
