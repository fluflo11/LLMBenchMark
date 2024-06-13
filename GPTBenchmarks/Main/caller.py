import sys
import subprocess


def main(prompt_txt,tikz_tex,perf_img,perf_tikz):
    print('\n' + 'Tikz compilation ------------' + '\n')
    subprocess.run('python3 tikzcompiler.py ' + tikz_tex)
    print('\n' +'Chatgptcaller ------------' + '\n')
    subprocess.run('python3 chatgptcaller.py' + tikz_tex + ' '+ prompt_txt)
    print('\n' +' Diff ------------' + '\n')
    subprocess.run('python3 diff.py ' + 
                    'Ressources/Tikz/tikz_res.tex' + ' ' +
                    perf_tikz + ' ' + 
                    'Ressources/Tikz/tikz_res.png' + ' ' +
                    perf_img )
    

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Params to use the script : prompt_txt,tikz_tex,perf_img,perf_tikz")
    else:
        prompt_txt = sys.argv[1]
        tikz_tex = sys.argv[2]
        perf_img = sys.argv[3]
        perf_tikz = sys.argv[4]
        main(prompt_txt,tikz_tex, perf_img, perf_tikz)
