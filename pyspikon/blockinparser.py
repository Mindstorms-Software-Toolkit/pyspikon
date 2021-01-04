import json
def recursion_parse(inputs):
    for i, c in enumerate(inputs):
        data = json.load(open('project.json'))
        if c in data['targets'][1]['blocks']:
            values = []
            for v in list(data['targets'][1]['blocks'][c]['inputs'].values()):
                if type(v)==str:
                    values.append(v)
                elif type(v[1]) == str:
                    values.append(v[1])
                else:
                    values.append(v[1][1])
            inputs[i:1] = parse(data['targets'][1]['blocks']
                                [c]['opcode'], values, values)
    return inputs
def operator_add(inputs):
    # (inputs)
    for i, c in enumerate(inputs):
        recursion_parse(inputs)
        #(parse(data['targets'][1]['blocks'][c]['opcode'], values))
    # (inputs)
    return [inputs[0]+"+"+inputs[1]]
def operator_subtract(inputs):
    for i, c in enumerate(inputs):
        recursion_parse(inputs)
    return [inputs[0]+"-"+inputs[1]]
def operator_multiply(inputs):
    recursion_parse(inputs)
    return [inputs[0]+"*"+inputs[1]]
def operator_divide(inputs):
    recursion_parse(inputs)
    return [inputs[0]+"/"+inputs[1]]
def operator_random(inputs):
    pass
def operator_lt(inputs):
    recursion_parse(inputs)
    return [inputs[0]+"<"+inputs[1]]
def operator_equals(inputs):
    recursion_parse(inputs)
    return [inputs[0]+"="+inputs[1]]
def operator_gt(inputs):
    recursion_parse(inputs)
    return [inputs[0]+">"+inputs[1]]
def operator_and(inputs):
    return inputs
def operator_or(inputs):
    return inputs
def operator_not(inputs):
    return inputs
def flipperoperator_isInBetween(inputs):
    recursion_parse(inputs)
    return [inputs[1]+">="+inputs[0]+">="+inputs[2]]
def operator_join(inputs):
    recursion_parse(inputs)
    return ["'"+inputs[0]+"'.join('"+inputs[1]+"')"]
def operator_letter_of(inputs):
    recursion_parse(inputs)
    return [inputs[1]+"["+inputs[0]+"]"]
def operator_length(inputs):
    recursion_parse(inputs)
    return ["len("+inputs[0]+")"]
def operator_contains(inputs):
    recursion_parse(inputs)
    return [inputs[0]+" in "+inputs[1]]
def operator_round(inputs):
    recursion_parse(inputs)
    return ["round("+inputs[0]+")"]
def operator_mathop(inputs):
    recursion_parse(inputs)
    listops = ['abs', 'floor', 'ceiling', 'sqrt', 'sin', 'cos',
               'tan', 'asin', 'acos', 'atan', 'ln', 'log', 'e ^', '10 ^']
    listfuncs = [f'abs({inputs[0]})', f'floor({inputs[0]})', f'ceil({inputs[0]})', f'sqrt({inputs[0]})', f'sin({inputs[0]})', f'cos({inputs[0]})', f'tan({inputs[0]})',
                 f'asin({inputs[0]})', f'acos({inputs[0]})', f'atan({inputs[0]})', f'log({inputs[0]})', f'log({inputs[0]})', f'math.e**{inputs[0]}', f'10**{inputs[0]}']
    return [listfuncs[listops.index(inputs[1])]]
def flippersensors_timer(inputs):
    return ["timer.now()"]
def flippersensors_buttonIsPressed(inputs):
    return [f"hub.{inputs[0]}_button.is_pressed()"]
def flippersensors_ismotion(inputs):
    return inputs
def flippersensors_isorientation(inputs):
    return inputs
def flippersensors_distance(inputs):
    return ['distance.get_distance()']
def flippersensors_isDistance(inputs):
    recursion_parse(inputs)
    listtypes = ['%', 'cm', 'i']
    listfuncs = ['motor.get_distance_percentage()', 'motor.get_distance_cm()',
                 'motor.get_distance_inches()']
    return [listfuncs[listtypes.index(inputs[3])]+inputs[2]+inputs[1]]
def flippersensors_force(inputs):
    recursion_parse(inputs)
    return inputs
def flippersensors_isPressed(inputs):
    return ['force.is_pressed()']

def flippersensors_reflectivity(inputs):
    return ['color.get_reflected_light()']

def flippersensors_isReflectivity(inputs):
    recursion_parse(inputs)
    return ["color.get_reflected_light()"+inputs[2]+inputs[1]]

def flippersensors_color(inputs):
    return ['color.get_color()']

def flippersensors_isColor(inputs):
    recursion_parse(inputs)
    return ["color.get_color()"+inputs[2]+inputs[1]]

def sound_volume(inputs):
    return ['hub.speaker.get_volume()']

def flippermotor_absolutePosition(inputs):
    return ['motor.get_position()']

def flippermotor_speed(inputs):
    return ['motor.get_speed()']

def parse(opcode, inputs, ifnotfind=None):
    try:
        return eval(f'{opcode}({inputs})')
    except:
        return ifnotfind
