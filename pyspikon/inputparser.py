#PYSPIKON - PySpikeConverter
                                                                                
#INPUT PARSER - ANALIZADOR DE CÓDIGOS
#pyjonhact - 2020 | License GNU GPL v3
import ast

def flippermotor_motorGoDirectionToPosition(inputs):
    inputsnew=[]
    inputsnew.append(float(inputs[1]))
    if inputs[2] == "shortest":
        inputsnew.append("'Shortest path'")
    else:
        inputsnew.append("'"+inputs[2].capitalize()+"'")
    return inputsnew
def flippermotor_motorStartDirection(inputs):
    return [inputs[0] if len(inputs)==3 else inputs[1]]
def flippermotor_motorSetSpeed(inputs):
    return [int(inputs[2])]
def flippermove_move(inputs):
    checkin=4-len(inputs)
    inputsnew=[]
    inputsnew.append(float(inputs[2-checkin])*-1 if inputs[0]=='back' else float(inputs[2-checkin]))
    inputsnew.append("'"+inputs[3-checkin]+"'")
    strings=['forward', 'back', 'clockwise', 'counterclockwise']
    values=[0,0,100,-100]
    inputsnew.append(f'steering={values[strings.index(inputs[0])]}')
    return inputsnew
def flippermove_steer(inputs):
    checkin=4-len(inputs)
    inputsnew=[]
    inputsnew.append(float(inputs[2-checkin]))
    inputsnew.append("'"+inputs[3-checkin]+"'")
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
    checkin=4-len(inputs)
    return [float(inputs[0+checkin]), inputs[1+checkin]]
def flippersound_playSoundUntilDone(inputs):
    return ["'"+ast.literal_eval(inputs[0])['name']+"'"]
def flippersound_playSound(inputs):
    return ["'"+ast.literal_eval(inputs[0])['name']+"'"]
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
    return [inputs[0]]
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
    return ast.literal_eval(f'{opcode}({inputs})')