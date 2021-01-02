#PYSPIKON - PySpikeConverter
                                                                                
#MAIN CODE - CÓDIGO PRINCIPAL
#pyjonhact - 2020 | License GNU GPL v3

#Importa blibliotecas
import convert
import openzip
import argparse
import os.path, time


#Adiciona argumentos ao parser
parser = argparse.ArgumentParser(description='''PT-BR: Converte arquivos .llsp em códigos .py
EN: Convert .llsp files into .py codes''')
parser.add_argument('path', metavar='P', type=str,
                     help='''PT-BR: O caminho para o arquivo.
EN: The path to the file.''')
parser.add_argument('pypath', metavar='C', type=str,
                     help='''PT-BR: O repositorio onde o arquivo .py vai ser criado.
EN: The repository where the .py file will be created.''')
parser.add_argument('--live-editor', required=False, action='store_true',
                     help='''PT-BR: O repositorio onde o arquivo .py vai ser criado.
EN: The repository where the .py file will be created.''')
#Lê os argumentos extrai o arquivo project.json e o converte para .py
args = parser.parse_args()
file=args.path
last_time = time.ctime(os.path.getmtime(file))
if args.live_editor:
    print('Hit Ctrl+C to stop Live Editor')
    while(True):
        if time.ctime(os.path.getmtime(file)) != last_time:
            last_time = time.ctime(os.path.getmtime(file))
            p=convert.convert(openzip.extractandopen(args.path))
            c=args.pypath
            pythonfile = open(c+'\output.py', 'w+', encoding='utf-8')
            pythonfile.write(p)
            pythonfile.flush()
        time.sleep(1)
else:
    p=convert.convert(openzip.extractandopen(args.path))
    c=args.pypath
    pythonfile = open(c+'\output.py', 'w+', encoding='utf-8')
    pythonfile.write(p)