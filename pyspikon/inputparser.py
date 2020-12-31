#PYSPIKON - PySpikeConverter
                                                                                
#INPUT PARSER - ANALIZADOR DE CÓDIGOS
#pyjonhact - 2020 | License GNU GPL v3

#Importa blibliotecas
def flippermotor_motorGoDirectionToPosition(inputs):
    inputsnew=[]
    inputsnew.append(float(inputs[1]))
    if inputs[2] == "shortest":
        inputsnew.append("'Shortest path'")
    else:
        inputsnew.append("'"+inputs[2].capitalize()+"'")
    return inputsnew
def flippermotor_motorStartDirection(inputs):
    return [inputs[1]]
def flippermotor_motorSetSpeed(inputs):
    return [int(inputs[2])]
def flippermove_move(inputs):
    inputsnew=[]
    inputsnew.append(float(inputs[2])*-1 if inputs[0]=='backward' else float(inputs[2]))
    inputsnew.append("'"+inputs[3]+"'")
    strings=['forward', 'backward', 'clockwise', 'counterclockwise']
    values=[0,0,100,-100]
    inputsnew.append(f'steering={values[strings.index(inputs[0])]}')
    return inputsnew
def flippermove_steer(inputs):
    inputsnew=[]
    inputsnew.append(float(inputs[2]))
    inputsnew.append("'"+inputs[3]+"'")
    inputsnew.append(f'steering={int(inputs[0])}')
    return inputsnew
def flippermove_startSteer(inputs):
    inputsnew=[]
    inputsnew.append(f'steering={int(inputs[0])}')
    return inputsnew
def flippermove_stopMove(inputs):
    pass
def flippermove_movementSpeed(inputs):
    return [int(inputs[1])]
def flippermove_setMovementPair(inputs):
    return ["'"+item+"'" for item in list(inputs[0])]
def flippermove_setDistance(inputs):
    return [float(inputs[1]), inputs[2]]
def flippersound_playSoundUntilDone(inputs):
    return ["'"+eval(inputs[0])['name']+"'"]
def flippersound_playSound(inputs):
    return ["'"+eval(inputs[0])['name']+"'"]
def flippersound_beepForTime(inputs):
    return [int(inputs[0]), float(inputs[1])]
def flippersound_beep(inputs):
    return ['note='+inputs[0]]
def flippersound_stopSound(inputs):
    pass
def control_wait(inputs):
    return [float(inputs[0])]
def control_wait_until(inputs):
    pass
def flippersensors_resetYaw(inputs):
    pass
def flippersensors_resetTimer(inputs):
    pass
def flipperdisplay_ledText(inputs):
    return [inputs[1]]
def flipperdisplay_displayOff(inputs):
    pass
def flipperdisplay_ledOn(inputs):
    return[int(inputs[0]), int(inputs[1]), 'brightness='+inputs[3]]
def flipperdisplay_centerButtonLight(inputs):
    strings=["'black'", "'pink'", "'violet'", "'azure'", "'blue'", "'cyan'", "'green'", "'yellow'", "'orange'", "'red'", "'white'"]
    return [strings[int(inputs[0])]]
def flipperdisplay_ultrasonicLightUp(inputs):
    return map(int,inputs[1].split(" "))

def parse(opcode, inputs):
    return eval(f'{opcode}({inputs})')