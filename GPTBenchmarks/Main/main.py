import subprocess
import yaml


def parse_config(config_path):
    stream = open("../Ressources/Config/config.yaml",'r')
    config = yaml.load(stream)
    return config

def write_config(config_dict,config_path):
    with open(config_path,'w') as file:
        yaml.safe_dump(config_dict,file)

def update_config(config_path,key,value):
    config = parse_config(config_path)
    if key in config:
        config[key] = value
    write_config(config,config_path)
    

def main():

    config_path = '../Ressources/Config/config.yaml'
    config = parse_config(config_path)

    if config.get('first_time_used')==1:
        subprocess.call(['pip','install','-r','../Ressources/Dependencies/dependencies.txt'])
        subprocess.call(['sudo','apt-get','install','texlive-latex-base'])
        update_config(config_path,'first_time_used',0)


    iterations = int(config.get('number_of_test_iterations'),'1')
    command = ['python3','caller.py','../Ressources/Prompts/prompt.txt',
                  '../Ressources/Tikz/onlydog.tex','../Ressources/Tikz/onlydog_modified.pdf',
                  '../Ressources/Tikz/onlydog_modified.tex']
    for i in range(iterations):
        subprocess.call(command)

    
        
    

    


        
    
    

    
