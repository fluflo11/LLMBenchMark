from openai import OpenAI
import os
import sys
import subprocess

client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))


def call_chatgpt(prompt):


    response = client.completions.create(engine="gpt-3.5-turbo",
    prompt=prompt,
    max_tokens=2048,
    n=1,
    stop=None,
    temperature=0.2)

    return response.choices[0].text.strip()

def main(tex_file, prompt_file):

    with open(tex_file, 'r') as file:
        tex_content = file.read()
    with open(prompt_file, 'r') as file:
        prompt_content = file.read()

    prompt = f"{prompt_content}\n\n{tex_content}"
    result = call_chatgpt(prompt)

    os.makedirs('Ressources', exist_ok=True)
    with open('Ressources/Tikz/tikz_res.tex', 'w') as file: #res
        file.write(result)
    subprocess.run('python3 tikzcompiler.py Ressources/Tikz/tikz_res.tex')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Command to use the script : python3 chatgptcaller.py <tex_file> <prompt_file>")
    else:
        tex_file = sys.argv[1]
        prompt_file = sys.argv[2]
        main(tex_file, prompt_file)
