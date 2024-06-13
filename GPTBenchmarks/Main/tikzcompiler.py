import sys
import subprocess
import os

def compile_tex_to_pdf(tex_file):
    if not tex_file.endswith('.tex'):
        print("error: format needs to be .tex")
        return None
    
    output_dir = os.path.join('..', 'Ressources', 'Tikz')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    file_base = os.path.splitext(os.path.basename(tex_file))[0]  # Ensure only the filename is used
    pdf_output_path = os.path.join(output_dir, f"{file_base}.pdf")
    
    try:
        subprocess.run(['pdflatex', '-output-directory', output_dir, tex_file], check=True)
        print(f"file: {pdf_output_path}")
        return pdf_output_path
    except subprocess.CalledProcessError as e:
        print(f"error: {e}")
        return None
    finally:
        for ext in ['aux', 'log']:
            aux_log_path = os.path.join(output_dir, f"{file_base}.{ext}")
            try:
                os.remove(aux_log_path)
            except OSError:
                pass

def convert_to_img(pdf):
    output_dir = '../Ressources/Tikz'
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, os.path.basename(pdf).replace('.pdf', '.jpg'))
    
    command_convert = f'convert -density 300 -trim "{pdf}" -quality 100 "{output_file}"'
    try:
        subprocess.run(command_convert, shell=True, check=True, text=True)
        print(f"file: {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("command to use: python3 tikzcompiler.py <fichier.tex>")
    else:
        tex_file = sys.argv[1]
        pdf_file = compile_tex_to_pdf(tex_file)
        if pdf_file:
            convert_to_img(pdf_file)
