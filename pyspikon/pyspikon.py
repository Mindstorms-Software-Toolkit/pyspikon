#PYSPIKON - PySpikeConverter

# MAIN CODE - CÓDIGO PRINCIPAL
# pyjonhact - 2020 | License GNU GPL v3

# Importa blibliotecas
import convert
import openzip
import argparse
import os.path
import time
import shutil
start = time.time()

class InvalidRobotError(Exception):
    __module__ = 'pyspikerr'
    def __init__(self, robot=""):
        self.message = 'Invalid robot:'+robot+'!'
        super().__init__(self.message)

class InvalidFileOutputError(Exception):
    __module__ = 'pyspikerr'
    def __init__(self, output=""):
        self.message = 'Invalid output type:'+output+'!'
        super().__init__(self.message)

class LiveEditorNotSupportedError(Exception):
    __module__ = 'pyspikerr'
    def __init__(self, output=""): 
        self.message = 'Output type '+output+' does not support Live Editor!'
        super().__init__(self.message)
# Adiciona argumentos ao parser
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
parser.add_argument('--robot', required=False, default='Spike',
                    help='''PT-BR: O repositorio onde o arquivo .py vai ser criado.
EN: The repository where the .py file will be created.''')
parser.add_argument('--output', required=False, default='Python',
                    help='''PT-BR: O repositorio onde o arquivo .py vai ser criado.
EN: The repository where the .py file will be created.''')
# Lê os argumentos extrai o arquivo project.json e o converte para .py
args = parser.parse_args()
file = args.path
last_time = time.ctime(os.path.getmtime(file))
origin='.llsp' if args.robot == 'Spike' else '.lms'
codestart='''from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

hub = PrimeHub()'''if args.robot == 'Spike' else'''from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
import math

hub = MSHub() '''
origin='.llsp' if args.robot == 'Spike' else '.lms'

validrobots=['Spike', 'Inventor']
validoutputs=['Python', 'Spike', 'Inventor']
if not args.robot in validrobots:
    raise InvalidRobotError(args.robot)
if not args.output in validoutputs:
    raise InvalidFileOutputError(args.output)
if args.output=='Python':
    if args.live_editor:
        print('Hit Ctrl+C to stop Live Editor')
        while(True):
            if time.ctime(os.path.getmtime(file)) != last_time:
                last_time = time.ctime(os.path.getmtime(file))
                p = convert.convert(openzip.extractandopen(args.path, origin), codestart)
                c = args.pypath
                pythonfile = open(c+'\output.py', 'w+', encoding='utf-8')
                pythonfile.write(p)
                pythonfile.flush()
            time.sleep(1)
    else:
        p = convert.convert(openzip.extractandopen(args.path, origin), codestart)
        c = args.pypath
        pythonfile = open(c+'\output.py', 'w+', encoding='utf-8')
        pythonfile.write(p)

    print(f'Time elapsed: {time.time() - start}')
else:
    output='.llsp' if args.output == 'Spike' else '.lms'
    shutil.copyfile(args.path, args.pypath+'output'+output)
    print(args.path, args.pypath+'\output'+output)