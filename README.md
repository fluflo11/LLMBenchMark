
# End User LLM Benchmark Tool
A flexible and easily adaptable tool for testing the reliability of Large Language Models in code modification. 
The code provided here allows you to test the modification of tikz files with GPT 3.5 turbo. 





## Usage

The code was designed and tested with python 3.10.12.
The code's dependencies will be installed automatically the first time you use it. 

To use the code, first modify the bench.yaml file

Example :

```yaml
parameters:
  - prompt: "your_prompt_here"
    tikz: "../Ressources/Tikz/your_file.tex"
    perf_tikz: "../Ressources/Tikz/your_perfect_file.tex"

```

Then execute main.py without any arguments.

You can modify the various code parameters by editing the config.yaml file.
For example, you can change the LLM temperature: 

```yaml
    #Default
    temperature : 0.2
    #Modified
    temperature : 0.8
```
Notice that you need to set up your OPENAI API key as an environment variable named ```OPENAI_API_KEY``` ([ See this guide for more informations ](https://www3.ntu.edu.sg/home/ehchua/programming/howto/Environment_Variables.html#:~:text=To%20set%20an%20environment%20variable,set%20varname%20%3Dvalue%20%22)). 




## Files and Modularity

The file main.py reads the ```config.yaml``` file and install all the dependencies if this is the first time the program is used. 

Several benchmarks can be listed in the ```benchs.yaml``` file (see Usage/Examples). 

For each benchmark, ```main.py``` will call ```caller.py``` with the parameters specific to that benchmark. 

```caller.py``` will then compile the tikz file ("tikz" in ```benchs.yaml```), call an LLM with the prompt ("prompt" in ```benchs.yaml```) passed as a parameter, compile the LLM result and then perform a difference between the results and the ground truth ("perf_tikz" in ```benchs.yaml```). 

The results will be stored in a yaml in the ```Resources/Results``` folder so that they can be reused later for statistical purposes.
## Acknowledgements

 - [LLM and VLM-assisted code modification](https://github.com/UN-L/EndUserLLM)

 - [A Demonstration of End-User Code Customization Using Generative AI](https://docs.google.com/presentation/d/1La9sS2VbiEybJxC7qoJD3CvWazR-GIc_-5R72I11n7U/edit#slide=id.g2b65b618a6a_5_780)

## Dependencies

- [opencv-python](https://pypi.org/project/opencv-python/)
- [numpy](https://numpy.org/)
- [python-Levenshtein 0.25.1](https://pypi.org/project/python-Levenshtein/)
- [openai](https://github.com/openai/openai-python)
