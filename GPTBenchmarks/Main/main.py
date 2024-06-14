import subprocess
import yaml
import sys


def read_yaml(file_path):
    with open(file_path, "r") as file:
        data = yaml.safe_load(file)
    return data

def write_config(config_dict,config_path):
    with open(config_path,'w') as file:
        yaml.safe_dump(config_dict,file)

def update_config(config_path,key,value):
    config = read_yaml(config_path)
    if key in config:
        config[key] = value
    write_config(config,config_path)
    

def main():

    config_path = '../Ressources/Config/config.yaml'
    config = read_yaml(config_path)

    if config.get('first_time_used')==1:
        subprocess.call(['pip','install','-r','../Ressources/Dependencies/dependencies.txt'])
        subprocess.call(['sudo','apt-get','install','texlive-latex-base'])
        update_config(config_path,'first_time_used',0)
    
    benchs_path = '../Ressources/Benchmarks/benchs.yaml'
    benchs = read_yaml(benchs_path)
    
    parameters = benchs.get("parameters",[])

    for index, param in enumerate(parameters,start=1):
        prompt = param.get("prompt")
        tikz = param.get("tikz")
        perf_tikz = param.get("perf_tikz")
        command = ['python3','caller.py',prompt,tikz,perf_tikz]
        subprocess.call(command)


if __name__ == "__main__":
    if len(sys.argv) != 1:
        print("Main doesnt take any arguments. Modify benchs.yaml and config.yaml")
    else:
        main()
    
        
    

    


        
    
    

    
