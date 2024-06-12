import sys
import subprocess
import os


def compile_tex_to_pdf(tex_file):
    if not tex_file.endswith('.tex'):
        print("error : format need to be .tex")
        return
    file_base = os.path.splitext(tex_file)[0]
    try:
        subprocess.run(['pdflatex', tex_file], check=True)
        print(f"file : {file_base}.pdf")
    except subprocess.CalledProcessError as e:
        print(f"error : {e}")
    finally:
        for ext in ['aux', 'log']:
            try:
                os.remove(f"{file_base}.{ext}")
            except OSError:
                pass


def convert_to_img(pdf):
    command_convert = f'convert -density 300 -trim {pdf} -quality 100 {pdf.replace(".pdf", ".jpg")}'
    try:
        subprocess.run(command_convert, shell=True, check=True, text=True)
        print(f"file : {pdf.replace('.pdf', '.jpg')}")
    except subprocess.CalledProcessError as e:
        print(f"error : {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("command to use : python3 tikzcompiler.py <fichier.tex>")
    else:
        tex_file = sys.argv[1]
        pdf_file = compile_tex_to_pdf(tex_file)
        if pdf_file:
            convert_to_img(pdf_file)
        

