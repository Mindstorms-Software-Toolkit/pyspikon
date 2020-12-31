#PYSPIKON - PySpikeConverter
                                                                                
#CODE CONVERTER - CONVERSOR DE CÓDIGOS
#pyjonhact - 2020 | License GNU GPL v3

#Importa blibliotecas
import json
from numpy import mat,array
import inputparser as parser

#Define a lista de conversão de funções
functionslist=[['flippermotor_motorGoDirectionToPosition', 'motor.run_to_position()'], ['flippermotor_motorStartDirection', 'motor.start()'], ['flippermotor_motorSetSpeed', 'motor.set_default_speed()'], ['flippermove_move', 'motor_pair.move()'], ['flippermove_steer', 'motor_pair.move_tank()'], ['flippermove_startSteer', 'motor_pair.start_tank()'], ['flippermove_stopMove', 'motor_pair.stop()'], ['flippermove_movementSpeed', 'motor_pair.set_default_speed()'], ['flippermove_setMovementPair', 'motor_pair = MotorPair()'], ['flippermove_setDistance', 'motor_pair.set_motor_rotation()'], ['flippersound_playSoundUntilDone', 'app.start_sound()'], ['flippersound_playSound', 'app.play_sound()'], ['flippersound_beepForTime', 'hub.speaker.beep()'], ['flippersound_beep', 'hub.speaker.start_beep()'], ['flippersound_stopSound', 'hub.speaker.stop()'], ['control_wait', 'wait_for_seconds()'], ['control_wait_until', 'wait_until()'], ['flippersensors_resetYaw', 'hub.motion_sensor.reset_yaw_angle()'], ['flippersensors_resetTimer', 'timer.reset()'],['flipperdisplay_ledText', 'hub.light_matrix.write()'],['flipperdisplay_displayOff', 'hub.light_matrix.off()'],['flipperdisplay_ledOn', 'hub.light_matrix.set_pixel()'], ['flipperdisplay_centerButtonLight', 'hub.status_light.on()'], ['flipperdisplay_ultrasonicLightUp', 'distance_sensor.light_up()']]

#Define a função de conversão
def convert(jsonobj):
    #Carrega dados
    data = json.load(jsonobj)
    #Define a base do programa .py
    program='''from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

hub = PrimeHub() 
app = App()
motor = Motor('A')
motor_pair = MotorPair('B', 'A')
distance_sensor = DistanceSensor('C')
color = ColorSensor('D')
force = ForceSensor('E')

'''
    for v in data['targets'][1]['variables']:
        program=program+(str(data['targets'][1]['variables'][v][0])+"="+str(data['targets'][1]['variables'][v][1]))+'\n'
    for l in data['targets'][1]['lists']:
        program=program+(str(data['targets'][1]['lists'][l][0])+"="+str(data['targets'][1]['lists'][l][1]))+'\n'
    #Verifica todos os blocos listados
    for i in data['targets'][1]['blocks']:
        #Verifica se existe algum comentario para o bloco, se tiver, grava no programa.
        for comments in data['targets'][1]['comments']:
            if data['targets'][1]['comments'][comments]['blockId'] == i:
                program=program+'\n\n#'+data['targets'][1]['comments'][comments]['text'].replace('\n', '\n#')
        #----VARIABLES/LISTS PARSER/ANALIZADOR DE VARIAVEIS/LISTAS----#
        if data['targets'][1]['blocks'][i]['opcode'] == "data_setvariableto":
            variable=str(data['targets'][1]['blocks'][i]['fields']['VARIABLE'][0])
            value=str(data['targets'][1]['blocks'][i]['inputs']['VALUE'][1][1])
            program=f"{program}{variable}='{value}'\n" if not value.isnumeric else f"{program}{variable}={value}\n" 
        if data['targets'][1]['blocks'][i]['opcode'] == "data_changevariableby":
            variable=str(data['targets'][1]['blocks'][i]['fields']['VARIABLE'][0])
            value=str(data['targets'][1]['blocks'][i]['inputs']['VALUE'][1][1])
            program=f"{program}{variable}+='{value}'\n" if not value.isnumeric else f"{program}{variable}+={value}\n" 
        if data['targets'][1]['blocks'][i]['opcode'] == "data_addtolist":
            listo=str(data['targets'][1]['blocks'][i]['fields']['LIST'][0])
            item=str(data['targets'][1]['blocks'][i]['inputs']['ITEM'][1][1])
            program=f"{program}{listo}.append('{item}')\n"
        if data['targets'][1]['blocks'][i]['opcode'] == "data_deleteoflist":
            listo=str(data['targets'][1]['blocks'][i]['fields']['LIST'][0])
            item=str(int(data['targets'][1]['blocks'][i]['inputs']['INDEX'][1][1])-1)
            program=f"{program}{listo}.pop({item})\n"
        if data['targets'][1]['blocks'][i]['opcode'] == "data_deletealloflist":
            listo=str(data['targets'][1]['blocks'][i]['fields']['LIST'][0])
            program=f"{program}{listo}=[]\n"
        if data['targets'][1]['blocks'][i]['opcode'] == "data_insertatlist":
            listo=str(data['targets'][1]['blocks'][i]['fields']['LIST'][0])
            item=str(data['targets'][1]['blocks'][i]['inputs']['ITEM'][1][1])
            index=str(int(data['targets'][1]['blocks'][i]['inputs']['INDEX'][1][1])-1)
            program=f"{program}{listo}.insert({index},'{item}')\n"
        #----LIGHT MATRIX PARSER/ANALIZADOR DA MATRIZ DE LUZ----#
        if data['targets'][1]['blocks'][i]['opcode'] == "flipperdisplay_ledImageFor":
            matrixlight=mat(array(list(data['targets'][1]['blocks'][data['targets'][1]['blocks'][i]["inputs"]['MATRIX'][1]]['fields']["field_flipperdisplay_custom-matrix"][0])))
            matrixlight=matrixlight.reshape(5,5)
            newmatrixlight=[]
            for ind in range(0,5):
                listmatrix=list(map(int, matrixlight.tolist()[ind]))
                listmatrix = [itemint * 10 for itemint in listmatrix]
                newmatrixlight.append(listmatrix)
            program=program+f"for indexrow, row in enumerate({str(newmatrixlight)}):\n   for indexcol, column in enumerate(row):\n      hub.light_matrix.set_pixel(indexrow, indexcol, brightness=column)\nwait_for_seconds({int(data['targets'][1]['blocks'][i]['inputs']['VALUE'][1][1])})\nhub.light_matrix.off()\n"
        if data['targets'][1]['blocks'][i]['opcode'] == "flipperdisplay_ledImage":
            matrixlight=mat(array(list(data['targets'][1]['blocks'][data['targets'][1]['blocks'][i]["inputs"]['MATRIX'][1]]['fields']["field_flipperdisplay_custom-matrix"][0])))
            matrixlight=matrixlight.reshape(5,5)
            newmatrixlight=[]
            for ind in range(0,5):
                listmatrix=list(map(int, matrixlight.tolist()[ind]))
                listmatrix = [itemint * 10 for itemint in listmatrix]
                newmatrixlight.append(listmatrix)
            program=program+f"for indexrow, row in enumerate({str(newmatrixlight)}):\n   for indexcol, column in enumerate(row):\n      hub.light_matrix.set_pixel(indexrow, indexcol, brightness=column)\n"
        #Verifica a lista de funções.
        for function in functionslist:
            #Define a lista de inputs.
            inputsfunc=[]
            #Verifica se o código de bloco está listado em functionslist.
            if data['targets'][1]['blocks'][i]['opcode'] == function[0]:
                #Verifica as inputs do bloco.
                for inputs in data['targets'][1]['blocks'][i]['inputs']:
                    #Verifica os valores das inputs
                    inputs2=data['targets'][1]['blocks'][i]['inputs'][inputs][1]
                    #Tenta ver se o valor leva a um menu seletor.
                    try:
                        if inputs2 in data['targets'][1]['blocks']:
                            #Grava as fields do menu seletor na lista de inputs..
                            for field in data['targets'][1]['blocks'][inputs2]['fields']:
                                inputsfunc.append(data['targets'][1]['blocks'][inputs2]['fields'][field][0])
                        else:
                            inputsfunc.append(inputs2)
                    except TypeError:
                        #Verifica se a input é uma lista, e repete o processo de verificação de inputs para cada item nessa lista
                        if isinstance(inputs2, list):
                            for inputf in inputs2:
                                try:
                                    if inputf in data['targets'][1]['blocks']:
                                        for field in data['targets'][1]['blocks'][inputf]['fields']:
                                            inputsfunc.append(data['targets'][1]['blocks'][inputf]['fields'][field][0])
                                    else:
                                        inputsfunc.append(inputf)
                                except TypeError:
                                    inputsfunc.append(inputf)
                        elif isinstance(inputs2, dict):
                            for inputf in inputs2:
                                try:
                                    if inputf in data['targets'][1]['blocks']:
                                        for field in data['targets'][1]['blocks'][inputf]['fields']:
                                            inputsfunc.append(data['targets'][1]['blocks'][inputf]['fields'][field][0])
                                    else:
                                        inputsfunc.append(inputf)
                                except TypeError:
                                    inputsfunc.append(inputf)
                        #Grava na lista a input se ela não for uma lista
                        else:
                            inputsfunc.append(inputs2)
                #Verifica as fields do bloco.
                for fields in data['targets'][1]['blocks'][i]['fields']:
                    #Verifica os valores das fields
                    fields2=data['targets'][1]['blocks'][i]['fields'][fields][0]
                    print(fields2)
                    #Tenta ver se o valor leva a um menu seletor.
                    try:
                        if fields2 in data['targets'][1]['blocks']:
                            #Grava as fields do menu seletor na lista de fields..
                            for field in data['targets'][1]['blocks'][fields2]['fields']:
                                inputsfunc.append(data['targets'][1]['blocks'][fields2]['fields'][field][0])
                        else:
                            inputsfunc.append(fields2)
                    except TypeError:
                        #Verifica se a field é uma lista, e repete o processo de verificação de fields para cada item nessa lista
                        if isinstance(fields2, list):
                            for fieldf in fields2:
                                try:
                                    if fieldf in data['targets'][1]['blocks']:
                                        for field in data['targets'][1]['blocks'][fieldf]['fields']:
                                            inputsfunc.append(data['targets'][1]['blocks'][fieldf]['fields'][field][0])
                                    else:
                                        inputsfunc.append(fieldf)
                                except TypeError:
                                    inputsfunc.append(fieldf)
                        elif isinstance(fields2, dict):
                            for fieldf in fields2:
                                print(fieldf)
                                try:
                                    if fieldf in data['targets'][1]['blocks']:
                                        for field in data['targets'][1]['blocks'][fieldf]['fields']:
                                            inputsfunc.append(data['targets'][1]['blocks'][fieldf]['fields'][field][0])
                                    else:
                                        inputsfunc.append(fieldf)
                                except TypeError:
                                    inputsfunc.append(fieldf)
                        #Grava na lista a field se ela não for uma lista
                        else:
                            inputsfunc.append(fields2)
                #Cria uma outra string baseada na função referente ao bloco.
                functionmodify=function[1][:-1]
                #Parse inputs
                inputsfunc=parser.parse(data['targets'][1]['blocks'][i]['opcode'], inputsfunc)
                #Une a função e as inputs ao programa.
                print(inputsfunc)
                if inputsfunc == None:
                    inputsfunc=[]
                program=program+'\n'+functionmodify+','.join(str(ifunc) for ifunc in inputsfunc)+')'
    #Retorna o programa
    return program
