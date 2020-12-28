#PYSPIKON - PySpikeConverter
                                                                                
#MAIN CODE - CÓDIGO PRINCIPAL
#pyjonhact - 2020 | License GNU GPL v3

#Importa blibliotecas
import convert
import openzip
import argparse

#Adiciona argumentos ao parser
parser = argparse.ArgumentParser(description='''PT-BR: Converte arquivos .llsp em códigos .py
EN: Convert .llsp files into .py codes''')
parser.add_argument('path', metavar='P', type=str,
                     help='''PT-BR: O caminho para o arquivo.
EN: The path to the file.''')

#Lê os argumentos extrai o arquivo project.json e o converte para .py
args = parser.parse_args()
p=convert.convert(openzip.extractandopen(args.path))
pythonfile = open('output.py', 'w+', encoding='utf-8')
pythonfile.write(p)
