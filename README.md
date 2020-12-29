# **PySpikon**
PySpikon (a.k.a PySpikeConverter) is a Python-based program that allows you to convert .llsp files into .py files, it uses the *"project.json"* contained into your .llsp to create a Python file directly from the command-line.


PySpikon é um programa baseado em Python que te permite converter arquivos .llsp em arquivos .py, ele usa o *"project.json"* contido em seu .llsp para criar um arquivo Python direto da linha de comando

# Contents
1. [Installing (Windows)](#installing-windows)
2. [Installing (Linux)](#installing-linux)
3. [Use](#use)
### Installing (Windows)

To install PySpikon go to the releases page and download the .msi file. After downloading, run the file. This window will open:

![Window 1](https://i.imgur.com/9IGfJOA.png)

Click in **Next >**, now you will select the path where the program will be installed, the default path is Program Files, but you can change.

![Window 2](https://i.imgur.com/FFTkBXO.png)

After selecting the path click in **Next >** again and then in **Install**, now wait.

You will see the window below after install ends, just click on Finish.

![Window 3](https://i.imgur.com/gYEgGZG.png)

Now you are able to run PySpikon on Windows

### Installing (Linux)

Download [Git](https://git-scm.com/downloads), then run this on shell:
```
git clone https://github.com/pyjonhact/pyspikon.git
cd pyspikon
```
Now you are able to run PySpikon on Linux

### Use
To use it, run:
```bash
pyspikon path-to-file new-file-path
```
Or in Linux:
```bash
python setup.py path-to-file new-file-path
```
The output will be named "output.py"

