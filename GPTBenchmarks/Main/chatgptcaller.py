from openai import OpenAI
import os
import sys

client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))


def call_chatgpt(prompt,tex_file,sysgoal):

    

    messages_llm = [{"role": "system", "content":sysgoal},
                    {"role":"user", "content":tex_file},
                    {"role": "user", "content":prompt}]
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages = messages_llm,
    max_tokens=2048,
    n=1,
    stop=None,
    temperature=0.2,
    stream=False
    )
    return response.choices[0].message.content





def main(tex_file, prompt):

    with open(tex_file, 'r') as file:
        tex_content = file.read()

    sysgoal = "You are a helpful assistant for programming and customizing code. All you have to do is answer the question by writing the entire code with the modifications. To modify the code, use the comments. DO NOT answer anything other than the entire code. If you make mistakes, don't apologize, just send the entire code with the modifications"
    result = call_chatgpt(prompt,tex_content,sysgoal)
    
    
    os.makedirs('Ressources', exist_ok=True)
    with open('../Ressources/Tikz/tikz_res.tex', 'w') as file:
        file.write(result)



if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Command to use the script : python3 chatgptcaller.py <tex_file> <prompt_file>")
    else:
        tex_file = sys.argv[1]
        prompt = sys.argv[2]
        main(tex_file, prompt)
