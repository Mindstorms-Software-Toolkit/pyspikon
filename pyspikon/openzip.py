#PYSPIKON - PySpikeConverter
                                                                                
#ZIP UNMASKER - EXTRAIDOR DE ZIP
#pyjonhact - 2020 | License GNU GPL v3

#Importa blibliotecas
from zipfile import ZipFile
import shutil
import os

#Define a função de extração.
def extractandopen(directory):
    #Copia o arquivo como .zip e extrai o arquivo scratch.sb3
    shutil.copyfile(directory, directory.replace('.llsp', '.zip'))
    with ZipFile(directory.replace('.llsp', '.zip'), 'r') as zip:
        zip.extract('scratch.sb3')
    #Deleta o arquivo
    os.remove(directory.replace('.llsp', '.zip'))
    #Repete o mesmo processo com o arquivo scratch.sb3 
    with ZipFile('scratch.sb3', 'r') as zip:
        zip.extract('project.json')
    os.remove('scratch.sb3')
    #Retorna o arquivo project.json
    return open('project.json', encoding='utf-8')
