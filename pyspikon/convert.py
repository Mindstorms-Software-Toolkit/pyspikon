#PYSPIKON - PySpikeConverter

# CODE CONVERTER - CONVERSOR DE CÓDIGOS
# pyjonhact - 2020 | License GNU GPL v3

# Importa blibliotecas
import json
from numpy import mat, array
import inputparser as parser
import blockinparser as bparser
import itertools
# Define a lista de conversão de funções
functionslist = [['flippermotor_motorGoDirectionToPosition', 'motor.run_to_position()'], ['flippermotor_motorStartDirection', 'motor.start()'], ['flippermotor_motorSetSpeed', 'motor.set_default_speed()'], ['flippermove_move', 'motor_pair.move()'], ['flippermove_steer', 'motor_pair.move_tank()'], ['flippermove_startSteer', 'motor_pair.start_tank()'], ['flippermove_stopMove', 'motor_pair.stop()'], ['flippermove_movementSpeed', 'motor_pair.set_default_speed()'], ['flippermove_setMovementPair', 'motor_pair = MotorPair()'], ['flippermove_setDistance', 'motor_pair.set_motor_rotation()'], ['flippersound_playSoundUntilDone', 'app.start_sound()'], ['flippersound_playSound', 'app.play_sound()'], [
    'flippersound_beepForTime', 'hub.speaker.beep()'], ['flippersound_beep', 'hub.speaker.start_beep()'], ['flippersound_stopSound', 'hub.speaker.stop()'], ['control_wait', 'wait_for_seconds()'], ['control_wait_until', 'wait_until()'], ['flippersensors_resetYaw', 'hub.motion_sensor.reset_yaw_angle()'], ['flippersensors_resetTimer', 'timer.reset()'], ['flipperdisplay_ledText', 'hub.light_matrix.write()'], ['flipperdisplay_displayOff', 'hub.light_matrix.off()'], ['flipperdisplay_ledOn', 'hub.light_matrix.set_pixel()'], ['flipperdisplay_centerButtonLight', 'hub.status_light.on()'], ['flipperdisplay_ultrasonicLightUp', 'distance_sensor.light_up()']]

# Define a função de conversão


def convert(jsonobj):
    # Carrega dados
    data = json.load(jsonobj)
    # Define a base do programa .py
    program = '''from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
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

    def functionparse(i, program, lineseparator='\n'):
        for comments in data['targets'][1]['comments']:
            if data['targets'][1]['comments'][comments]['blockId'] == i:
                program = program+f'{lineseparator}{lineseparator}#' + data['targets'][1]['comments'][comments]['text'].replace('\n', f'{lineseparator}#')
        #----VARIABLES/LISTS PARSER/ANALIZADOR DE VARIAVEIS/LISTAS----#
        if data['targets'][1]['blocks'][i]['opcode'] == 'data_setvariableto':
            variable = str(data['targets'][1]['blocks']
                           [i]['fields']['VARIABLE'][0])
            value = data['targets'][1]['blocks'][i]['inputs']['VALUE'][1][1] if type(data['targets'][1]['blocks'][i]['inputs']['VALUE'][1]) == list else data['targets'][1]['blocks'][i]['inputs']['VALUE'][1]
            if value in data['targets'][1]['blocks']:
                inputsvalue = list(
                    data["targets"][1]["blocks"][value]['inputs'].values())
                fieldsvalue = list(
                    data['targets'][1]['blocks'][value]['fields'].values())
                inputsvalue = list([ic[1][1]
                                        for ic in inputsvalue])
                fieldsvalue = list([ic[0][0]
                                        for ic in fieldsvalue])
                value = bparser.parse(data['targets'][1]['blocks'][value]['opcode'], inputsvalue+fieldsvalue)
                program = f"{program}{lineseparator}{variable}={''.join(value)}"
            else:
                for ind, variabler, listr in itertools.zip_longest(itertools.count(), list(data['targets'][1]['variables']), list(data['targets'][1]['lists'])):
                    if variabler==None and listr==None:
                        break
                    if False if variabler==None else value == data['targets'][1]['variables'][variabler][0]:
                        program = f"{program}{lineseparator}{variable}={value}"
                        break
                    if False if listr==None else value == data['targets'][1]['lists'][listr][0]:
                        program = f"{program}{lineseparator}{variable}={value}"
                        break
                    elif ind == len(data['targets'][1]['variables'])-1:
                        value = str(data['targets'][1]['blocks'][i]['inputs']['VALUE'][1][1])
                        program = f"{program}{lineseparator}{variable}='{value}'" if not value.isnumeric() else f"{program}{variable}={value}{lineseparator}"
        elif data['targets'][1]['blocks'][i]['opcode'] == 'data_changevariableby':
            variable = str(data['targets'][1]['blocks']
                           [i]['fields']['VARIABLE'][0])
            value = data['targets'][1]['blocks'][i]['inputs']['VALUE'][1][1] if type(data['targets'][1]['blocks'][i]['inputs']['VALUE'][1]) == list else data['targets'][1]['blocks'][i]['inputs']['VALUE'][1]
            if value in data['targets'][1]['blocks']:
                inputsvalue = list(
                    data["targets"][1]["blocks"][value]['inputs'].values())
                fieldsvalue = list(
                    data['targets'][1]['blocks'][value]['fields'].values())
                inputsvalue = list([ic[1][1]
                                        for ic in inputsvalue])
                fieldsvalue = list([ic[0][0]
                                        for ic in fieldsvalue])
                value = bparser.parse(data['targets'][1]['blocks'][value]['opcode'], inputsvalue+fieldsvalue)
                program = f"{program}{lineseparator}{variable}+={''.join(value)}"
            else:
                for ind, variabler, listr in itertools.zip_longest(itertools.count(), list(data['targets'][1]['variables']), list(data['targets'][1]['lists'])):
                    if variabler==None and listr==None:
                        break
                    if False if variabler==None else value == data['targets'][1]['variables'][variabler][0]:
                        program = f"{program}{lineseparator}{variable}+={value}"
                        break
                    if False if listr==None else value == data['targets'][1]['lists'][listr][0]:
                        program = f"{program}{lineseparator}{variable}+={value}"
                        break
                    elif ind == len(data['targets'][1]['variables'])-1:
                        value = str(data['targets'][1]['blocks'][i]['inputs']['VALUE'][1][1])
                        program = f"{program}{lineseparator}{variable}+='{value}'" if not value.isnumeric() else f"{program}{lineseparator}{variable}={value}"
            
        elif data['targets'][1]['blocks'][i]['opcode'] == 'data_addtolist':
            listo = str(data['targets'][1]['blocks'][i]['fields']['LIST'][0])
            item = data['targets'][1]['blocks'][i]['inputs']['ITEM'][1][1] if type(data['targets'][1]['blocks'][i]['inputs']['ITEM'][1]) == list else data['targets'][1]['blocks'][i]['inputs']['ITEM'][1]
            if item in data['targets'][1]['blocks']:
                inputsitem = list(
                    data["targets"][1]["blocks"][item]['inputs'].items())
                fieldsitem = list(
                    data['targets'][1]['blocks'][item]['fields'].items())
                inputsitem = list([ic[1][1]
                                        for ic in inputsitem])
                fieldsitem = list([ic[0][0]
                                        for ic in fieldsitem])
                item = bparser.parse(data['targets'][1]['blocks'][item]['opcode'], inputsitem+fieldsitem)
                program = f"{program}{lineseparator}{listo}.append('{''.join(item)}')"
            else:
                for ind, variabler, listr in itertools.zip_longest(itertools.count(), list(data['targets'][1]['variables']), list(data['targets'][1]['lists'])):
                    if variabler==None and listr==None:
                        break
                    if False if variabler==None else item == data['targets'][1]['variables'][variabler][0]:
                        program = f"{program}{lineseparator}{listo}.append('{item}')"
                        break
                    if False if listr==None else item == data['targets'][1]['lists'][listr][0]:
                        program = f"{program}{lineseparator}{listo}.append('{item}')"
                        break
                    elif ind == len(data['targets'][1]['variables'])-1:
                        item = str(data['targets'][1]['blocks'][i]['inputs']['ITEM'][1][1])
                        program = f"{program}{lineseparator}{listo}.append('{item}')"
        elif data['targets'][1]['blocks'][i]['opcode'] == 'data_deleteoflist':
            listo = str(data['targets'][1]['blocks'][i]['fields']['LIST'][0])
            item = data['targets'][1]['blocks'][i]['inputs']['INDEX'][1][1] if type(data['targets'][1]['blocks'][i]['inputs']['INDEX'][1]) == list else data['targets'][1]['blocks'][i]['inputs']['INDEX'][1]
            if item in data['targets'][1]['blocks']:
                inputsitem = list(
                    data["targets"][1]["blocks"][item]['inputs'].items())
                fieldsitem = list(
                    data['targets'][1]['blocks'][item]['fields'].items())
                inputsitem = list([ic[1][1]
                                        for ic in inputsitem])
                fieldsitem = list([ic[0][0]
                                        for ic in fieldsitem])
                item = bparser.parse(data['targets'][1]['blocks'][item]['opcode'], inputsitem+fieldsitem)
                program = f"{program}{lineseparator}{listo}.pop('{''.join(item)}')"
            else:
                for ind, variabler, listr in itertools.zip_longest(itertools.count(), list(data['targets'][1]['variables']), list(data['targets'][1]['lists'])):
                    if variabler==None and listr==None:
                        break
                    if False if variabler==None else item == data['targets'][1]['variables'][variabler][0]:
                        program = f"{program}{lineseparator}{listo}.pop({item})"
                        break
                    if False if listr==None else item == data['targets'][1]['lists'][listr][0]:
                        program = f"{program}{lineseparator}{listo}.pop({item})"
                        break
                    elif ind == len(data['targets'][1]['variables'])-1:
                        item = str(data['targets'][1]['blocks'][i]['inputs']['INDEX'][1][1])
                        program = f"{program}{lineseparator}{listo}.pop('{item}')"
        elif data['targets'][1]['blocks'][i]['opcode'] == 'data_deletealloflist':
            listo = str(data['targets'][1]['blocks'][i]['fields']['LIST'][0])
            program = f'{program}{lineseparator}{listo}=[]'
        elif data['targets'][1]['blocks'][i]['opcode'] == 'data_insertatlist':
            listo = str(data['targets'][1]['blocks'][i]['fields']['LIST'][0])
            item = data['targets'][1]['blocks'][i]['inputs']['ITEM'][1][1] if type(data['targets'][1]['blocks'][i]['inputs']['ITEM'][1]) == list else data['targets'][1]['blocks'][i]['inputs']['ITEM'][1]
            index = data['targets'][1]['blocks'][i]['inputs']['INDEX'][1][1] if type(data['targets'][1]['blocks'][i]['inputs']['INDEX'][1]) == list else data['targets'][1]['blocks'][i]['inputs']['INDEX'][1]
            if item in data['targets'][1]['blocks'] or index in data['targets'][1]['blocks']:
                if item in data['targets'][1]['blocks']:
                    inputsitem = list(
                        data["targets"][1]["blocks"][item]['inputs'].items())
                    fieldsitem = list(
                        data['targets'][1]['blocks'][item]['fields'].items())
                    inputsitem = list([ic[1][1]
                                            for ic in inputsitem])
                    fieldsitem = list([ic[0][0]
                                            for ic in fieldsitem])
                    item = bparser.parse(data['targets'][1]['blocks'][item]['opcode'], inputsitem+fieldsitem)
                if index in data['targets'][1]['blocks']:
                    inputsindex = list(
                        data["targets"][1]["blocks"][index]['inputs'].items())
                    fieldsindex = list(
                        data['targets'][1]['blocks'][index]['fields'].items())
                    inputsindex = list([ic[1][1]
                                            for ic in inputsindex])
                    fieldsindex = list([ic[0][0]
                                            for ic in fieldsindex])
                    index = bparser.parse(data['targets'][1]['blocks'][index]['opcode'], inputsindex+fieldsindex)
                program = f"{program}{lineseparator}{listo}.index({index if type(index)!=list else ''.join(index)}, {item if type(item)!=list else ''.join(item)})"
            else:
                for ind, variabler, listr in itertools.zip_longest(itertools.count(), list(data['targets'][1]['variables']), list(data['targets'][1]['lists'])):
                    if variabler==None and listr==None:
                        break
                    if False if variabler==None else item == data['targets'][1]['variables'][variabler][0]:
                        program = f"{program}{listo}.index({index}, {item}){lineseparator}"
                        break
                    if False if listr==None else item == data['targets'][1]['lists'][listr][0]:
                        program = f"{program}{listo}.index({index}, {item}){lineseparator}"
                        break
                    elif ind == len(data['targets'][1]['variables'])-1:
                        item = str(data['targets'][1]['blocks'][i]['inputs']['ITEM'][1][1])
                        program = f"{program}{listo}.index('{index}, '{item}'){lineseparator}"
        #----LIGHT MATRIX PARSER/ANALIZADOR DA MATRIZ DE LUZ----#
        elif data['targets'][1]['blocks'][i]['opcode'] == 'flipperdisplay_ledImageFor':
            matrixlight = mat(array(list(data['targets'][1]['blocks'][data['targets'][1]['blocks']
                                                                      [i]['inputs']['MATRIX'][1]]['fields']['field_flipperdisplay_custom-matrix'][0])))
            matrixlight = matrixlight.reshape(5, 5)
            newmatrixlight = []
            for ind in range(0, 5):
                listmatrix = list(map(int, matrixlight.tolist()[ind]))
                listmatrix = [itemint * 10 for itemint in listmatrix]
                newmatrixlight.append(listmatrix)
            secs = data['targets'][1]['blocks'][i]['inputs']['VALUE'][1][1] if type(data['targets'][1]['blocks'][i]['inputs']['VALUE'][1]) == list else data['targets'][1]['blocks'][i]['inputs']['VALUE'][1]
            if secs in data['targets'][1]['blocks']:
                inputssecs = list(
                    data["targets"][1]["blocks"][secs]['inputs'].secss())
                fieldssecs = list(
                    data['targets'][1]['blocks'][secs]['fields'].secss())
                inputssecs = list([ic[1][1]
                                        for ic in inputssecs])
                fieldssecs = list([ic[0][0]
                                        for ic in fieldssecs])
                secs = bparser.parse(data['targets'][1]['blocks'][secs]['opcode'], inputssecs+fieldssecs)
                program = program + \
                f'{lineseparator}for indexrow, row in enumerate({str(newmatrixlight)}):{lineseparator}    for indexcol, column in enumerate(row):{lineseparator}      hub.light_matrix.set_pixel(indexrow, indexcol, brightness=column){lineseparator}wait_for_seconds({"".join(secs)}){lineseparator}hub.light_matrix.off()'
            else:
                for ind, variabler, listr in itertools.zip_longest(itertools.count(), list(data['targets'][1]['variables']), list(data['targets'][1]['lists'])):
                    if variabler==None and listr==None:
                        if ind == max(0, len(data['targets'][1]['variables'])-1):
                            secs= str(data['targets'][1]['blocks'][i]['inputs']['VALUE'][1][1])
                            program = program + \
                            f'{lineseparator}for indexrow, row in enumerate({str(newmatrixlight)}):{lineseparator}    for indexcol, column in enumerate(row):{lineseparator}      hub.light_matrix.set_pixel(indexrow, indexcol, brightness=column){lineseparator}wait_for_seconds({secs}){lineseparator}hub.light_matrix.off()'
                        break
                    if False if variabler==None else secs == data['targets'][1]['variables'][variabler][0]:
                        program = program + \
                f'{lineseparator}for indexrow, row in enumerate({str(newmatrixlight)}):{lineseparator}    for indexcol, column in enumerate(row):{lineseparator}      hub.light_matrix.set_pixel(indexrow, indexcol, brightness=column){lineseparator}wait_for_seconds({secs}){lineseparator}hub.light_matrix.off()'
                        break
                    if False if listr==None else secs == data['targets'][1]['lists'][listr][0]:
                        program = program + \
                f'{lineseparator}for indexrow, row in enumerate({str(newmatrixlight)}):{lineseparator}    for indexcol, column in enumerate(row):{lineseparator}      hub.light_matrix.set_pixel(indexrow, indexcol, brightness=column){lineseparator}wait_for_seconds({secs}){lineseparator}hub.light_matrix.off()'
                        break
                    elif ind == len(data['targets'][1]['variables'])-1:
                        secs= str(data['targets'][1]['blocks'][i]['inputs']['VALUE'][1][1])
                        program = program + \
                        f'{lineseparator}for indexrow, row in enumerate({str(newmatrixlight)}):{lineseparator}    for indexcol, column in enumerate(row):{lineseparator}      hub.light_matrix.set_pixel(indexrow, indexcol, brightness=column){lineseparator}wait_for_seconds({secs}){lineseparator}hub.light_matrix.off()'
        elif data['targets'][1]['blocks'][i]['opcode'] == 'flipperdisplay_ledImage':
            matrixlight = mat(array(list(data['targets'][1]['blocks'][data['targets'][1]['blocks']
                                                                      [i]['inputs']['MATRIX'][1]]['fields']['field_flipperdisplay_custom-matrix'][0])))
            matrixlight = matrixlight.reshape(5, 5)
            newmatrixlight = []
            for ind in range(0, 5):
                listmatrix = list(map(int, matrixlight.tolist()[ind]))
                listmatrix = [itemint * 10 for itemint in listmatrix]
                newmatrixlight.append(listmatrix)
            program = program + \
                f'{lineseparator}for indexrow, row in enumerate({str(newmatrixlight)}):{lineseparator}   for indexcol, column in enumerate(row):{lineseparator}      hub.light_matrix.set_pixel(indexrow, indexcol, brightness=column){lineseparator}'
        else:
            for function in functionslist:
                # Define a lista de inputs.
                inputsfunc = []
                inputsrepl = []
                # Verifica se o código de bloco está listado em functionslist.
                if data['targets'][1]['blocks'][i]['opcode'] == function[0]:
                    # Verifica as inputs do bloco.
                    for inputs in data['targets'][1]['blocks'][i]['inputs']:
                        # Verifica os valores das inputs
                        inputs2 = data['targets'][1]['blocks'][i]['inputs'][inputs][1]
                        # Tenta ver se o valor leva a um menu seletor.
                        try:
                            if inputs2 in data['targets'][1]['variables']:
                                inputsrepl.append((data['targets'][1]['variables'][inputs2][0], len(inputsfunc)))
                                inputsfunc.append(len(inputsfunc)*123)
                            if inputs2 in data['targets'][1]['lists']:
                                inputsrepl.append((data['targets'][1]['lists'][inputs2][0], len(inputsfunc)))
                                inputsfunc.append(len(inputsfunc)*123)
                            if inputs2 in data['targets'][1]['blocks']:
                                valuestest = []
                                try:
                                    for v in list(data['targets'][1]['blocks'][inputs2]['inputs'].values()):
                                        if type(v) == str:
                                            valuestest.append(v)
                                        elif type(v[0]) == str:
                                            valuestest.append(v[0])
                                        else:
                                            valuestest.append(v[1][1])
                                except:
                                    pass
                                try:
                                    for v in list(data['targets'][1]['blocks'][inputs2]['fields'].values()):
                                        if type(v) == str:
                                            valuestest.append(v)
                                        elif type(v[0]) == str:
                                            valuestest.append(v[0])
                                        else:
                                            valuestest.append(v[0][0])
                                except:
                                    pass
                                valuesparsed = bparser.parse(
                                    data['targets'][1]['blocks'][inputs2]['opcode'], valuestest)
                                if valuesparsed != None:
                                    for field in valuesparsed:
                                        inputsrepl.append((field, len(inputsfunc)))
                                        inputsfunc.append(len(inputsfunc)*123)
                                else:
                                    # Grava as fields do menu seletor na lista de inputs.
                                    for field in valuestest:
                                        inputsfunc.append(field)
                            else:
                                inputsfunc.append(inputs2)
                        except TypeError:
                            # Verifica se a input é uma lista, e repete o processo de verificação de inputs para cada item nessa lista
                            if isinstance(inputs2, list):
                                for inputf in inputs2:
                                    try:
                                        if inputf in data['targets'][1]['blocks']:
                                            for field in data['targets'][1]['blocks'][inputf]['fields']:
                                                inputsfunc.append(
                                                    data['targets'][1]['blocks'][inputf]['fields'][field][0])
                                        else:
                                            inputsfunc.append(inputf)
                                    except TypeError:
                                        inputsfunc.append(inputf)
                            elif isinstance(inputs2, dict):
                                for inputf in inputs2:
                                    try:
                                        if inputf in data['targets'][1]['blocks']:
                                            for field in data['targets'][1]['blocks'][inputf]['fields']:
                                                inputsfunc.append(
                                                    data['targets'][1]['blocks'][inputf]['fields'][field][0])
                                        else:
                                            inputsfunc.append(inputf)
                                    except TypeError:
                                        inputsfunc.append(inputf)
                            # Grava na lista a input se ela não for uma lista
                            else:
                                inputsfunc.append(inputs2)
                    # Verifica as fields do bloco.
                    for fields in data['targets'][1]['blocks'][i]['fields']:
                        # Verifica os valores das fields
                        fields2 = data['targets'][1]['blocks'][i]['fields'][fields][0]
                        # Tenta ver se o valor leva a um menu seletor.
                        try:
                            if fields2 in data['targets'][1]['blocks']:
                                # Grava as fields do menu seletor na lista de fields..
                                for field in data['targets'][1]['blocks'][fields2]['fields']:
                                    inputsfunc.append(
                                        data['targets'][1]['blocks'][fields2]['fields'][field][0])
                            else:
                                inputsfunc.append(fields2)
                        except TypeError:
                            # Verifica se a field é uma lista, e repete o processo de verificação de fields para cada item nessa lista
                            if isinstance(fields2, list):
                                for fieldf in fields2:
                                    try:
                                        if fieldf in data['targets'][1]['blocks']:
                                            for field in data['targets'][1]['blocks'][fieldf]['fields']:
                                                inputsfunc.append(
                                                    data['targets'][1]['blocks'][fieldf]['fields'][field][0])
                                        else:
                                            inputsfunc.append(fieldf)
                                    except TypeError:
                                        inputsfunc.append(fieldf)
                            elif isinstance(fields2, dict):
                                for fieldf in fields2:
                                    try:
                                        if fieldf in data['targets'][1]['blocks']:
                                            for field in data['targets'][1]['blocks'][fieldf]['fields']:
                                                inputsfunc.append(
                                                    data['targets'][1]['blocks'][fieldf]['fields'][field][0])
                                        else:
                                            inputsfunc.append(fieldf)
                                    except TypeError:
                                        inputsfunc.append(fieldf)
                            # Grava na lista a field se ela não for uma lista
                            else:
                                inputsfunc.append(fields2)
                    # Cria uma outra string baseada na função referente ao bloco.
                    functionmodify = function[1][:-1]
                    # Parse inputs
                    inputsfunc = parser.parse(
                        data['targets'][1]['blocks'][i]['opcode'], inputsfunc)
                    # Une a função e as inputs ao programa.
                    if inputsfunc == None:
                        inputsfunc = []
                    if inputsrepl != None:
                        for item in inputsrepl:
                            inputsfunc[inputsfunc.index(item[1]*123)] = item[0]
                    program = program+lineseparator+functionmodify + \
                        ','.join(str(ifunc) for ifunc in inputsfunc)+')'
        return program
    for v in data['targets'][1]['variables']:
        program = program+(str(data['targets'][1]['variables'][v][0]) +
                           "="+str(data['targets'][1]['variables'][v][1]))+'\n'
    for l in data['targets'][1]['lists']:
        program = program+(str(data['targets'][1]['lists'][l][0]) +
                           "="+str(data['targets'][1]['lists'][l][1]))+'\n'
    # Verifica todos os blocos listados
    i = list(data['targets'][1]['blocks'].keys())[0]
    while i != None:
        # Verifica se existe algum comentario para o bloco, se tiver, grava no programa.
        def control_parser(i, program, lineseparator='\n'):
            if data['targets'][1]['blocks'][i]['opcode'] == "control_repeat":
                times = str(data['targets'][1]['blocks']
                            [i]['inputs']['TIMES'][1][1])
                program = program+f"{lineseparator}for c in range({times}):"
                try:
                    iif = data['targets'][1]['blocks'][i]['inputs']['SUBSTACK'][1]
                    while iif != None:
                        program = program+functionparse(iif, "", lineseparator+"    ") if functionparse(
                            iif, "", lineseparator+"    ") != "" and functionparse(
                            iif, "", lineseparator+"    ") != None else control_parser(iif, program, lineseparator+"    ")
                        iif = data['targets'][1]['blocks'][iif]['next']
                except:
                    pass
            if data['targets'][1]['blocks'][i]['opcode'] == "control_forever":
                program = program+f"{lineseparator}while True:"
                try:
                    iif = data['targets'][1]['blocks'][i]['inputs']['SUBSTACK'][1]
                    while iif != None:
                        program = program+functionparse(iif, "", lineseparator+"    ") if functionparse(
                            iif, "", lineseparator+"    ") != "" and functionparse(
                            iif, "", lineseparator+"    ") != None else control_parser(iif, program, lineseparator+"    ")
                        iif = data['targets'][1]['blocks'][iif]['next']
                except:
                    pass
            if data['targets'][1]['blocks'][i]['opcode'] == "control_if" or data['targets'][1]['blocks'][i]['opcode'] == "control_if_else":
                try:
                    inputscondition = list(
                        data['targets'][1]['blocks'][data['targets'][1]['blocks'][i]['inputs']['CONDITION'][1]]['inputs'].values())
                    fieldscondition = list(
                        data['targets'][1]['blocks'][data['targets'][1]['blocks'][i]['inputs']['CONDITION'][1]]['fields'].values())
                    inputscondition = list([ic[1] if ic[1] == str else ic[1][1]
                                            for ic in inputscondition])
                    fieldscondition = list([ic[0] if ic[0] == str else ic[0][0]
                                            for ic in fieldscondition])
                    condition = bparser.parse(data['targets'][1]['blocks'][data['targets'][1]['blocks']
                                                                           [i]['inputs']['CONDITION'][1]]['opcode'], inputscondition+fieldscondition)
                except:
                    condition = ""
                program = program + \
                    f"{lineseparator}if {condition if type(condition)!=list else ''.join(condition)}:"
                try:
                    iif = data['targets'][1]['blocks'][i]['inputs']['SUBSTACK'][1]
                    while iif != None:
                        program = program+functionparse(iif, "", lineseparator+"    ") if functionparse(
                            iif, "", lineseparator+"    ") != "" and functionparse(
                            iif, "", lineseparator+"    ") != None else control_parser(iif, program, lineseparator+"    ")
                        iif = data['targets'][1]['blocks'][iif]['next']
                except KeyError:
                    pass
                if data['targets'][1]['blocks'][i]['opcode'] == "control_if_else":
                    program = program+f"{lineseparator}else:"
                    try:
                        iif = data['targets'][1]['blocks'][i]['inputs']['SUBSTACK2'][1]
                        while iif != None:
                            program = program+functionparse(iif, "", lineseparator+"    ") if functionparse(
                                iif, "", lineseparator) != "" and functionparse(
                                iif, "", lineseparator) != None else control_parser(iif, program, lineseparator+"    ")
                            iif = data['targets'][1]['blocks'][iif]['next']
                    except:
                        pass
            if data['targets'][1]['blocks'][i]['opcode'] == "control_repeat_until":
                try:
                    inputscondition = list(
                        data['targets'][1]['blocks'][data['targets'][1]['blocks'][i]['inputs']['CONDITION'][1]]['inputs'].values())
                    fieldscondition = list(
                        data['targets'][1]['blocks'][data['targets'][1]['blocks'][i]['inputs']['CONDITION'][1]]['fields'].values())
                    inputscondition = list([ic[1] if ic[1] == str else ic[1][1]
                                            for ic in inputscondition])
                    fieldscondition = list([ic[0] if ic[0] == str else ic[0][0]
                                            for ic in fieldscondition])
                    condition = bparser.parse(data['targets'][1]['blocks'][data['targets'][1]['blocks']
                                                                           [i]['inputs']['CONDITION'][1]]['opcode'], inputscondition+fieldscondition)
                except:
                    condition = ""
                program = program + \
                    f"{lineseparator}while not {condition if type(condition)!=list else ''.join(condition)}:"
                try:
                    iif = data['targets'][1]['blocks'][i]['inputs']['SUBSTACK'][1]
                    while iif != None:
                        program = program+functionparse(iif, "", lineseparator+"    ") if functionparse(
                            iif, "", lineseparator+"    ") != "" and functionparse(
                            iif, "", lineseparator+"    ") != None else control_parser(iif, program, lineseparator+"    ")
                        iif = data['targets'][1]['blocks'][iif]['next']
                except KeyError:
                    pass
            return program
        fparseresults=functionparse(i, program)
        cparseresults=control_parser(i, program)
        program = fparseresults if fparseresults!=program else cparseresults if cparseresults!=program else program
        i = data['targets'][1]['blocks'][i]['next']
    # Retorna o programa
    return program
