# **PySpikon**
PySpikon is a Python package that allows you to convert .llsp files into .py files, it uses the *"project.json"* contained into your .llsp to create a Python file

PySpikon é um pacote do Python que te permite converter arquivos .llsp em arquivos .py, ele usa o *"project.json"* contido em seu .llsp para criar um arquivo python
### Installation

The only requirement to run PySpikon is [ArgParse](https://docs.python.org/3/library/argparse.html) 3.2.

To install PySpikon use:
```bash
pip install pyspikon
```

### Use

PySpikon cannot be imported. To use it, run:
```bash
python -m pyspikeconverter path-to-file new-file-path
```
The output will be named "output.py"

