import json
data = json.load(open('project.json'))


def operator_add(inputs):
    # (inputs)
    for i, c in enumerate(inputs):

        if c in data['targets'][1]['blocks']:
            values = []
            for v in list(data['targets'][1]['blocks'][c]['inputs'].values()):
                if type(v[1]) == str:
                    values.append(v[1])
                else:
                    values.append(v[1][1])
            inputs[i:1] = parse(data['targets'][1]['blocks']
                                [c]['opcode'], values, values)
            #(parse(data['targets'][1]['blocks'][c]['opcode'], values))
    # (inputs)
    return [inputs[0]+"+"+inputs[1]]


flippermotor_add = operator_add


def operator_subtract(inputs):
    for i, c in enumerate(inputs):

        if c in data['targets'][1]['blocks']:
            values = []
            for v in list(data['targets'][1]['blocks'][c]['inputs'].values()):
                if type(v[1]) == str:
                    values.append(v[1])
                else:
                    values.append(v[1][1])
            inputs[i:1] = parse(data['targets'][1]['blocks']
                                [c]['opcode'], values, values)
    return [inputs[0]+"-"+inputs[1]]


flippermotor_subtract = operator_subtract


def operator_multiply(inputs):
    for i, c in enumerate(inputs):

        if c in data['targets'][1]['blocks']:
            values = []
            for v in list(data['targets'][1]['blocks'][c]['inputs'].values()):
                if type(v[1]) == str:
                    values.append(v[1])
                else:
                    values.append(v[1][1])
            inputs[i:1] = parse(data['targets'][1]['blocks']
                                [c]['opcode'], values, values)
    return [inputs[0]+"*"+inputs[1]]


flippermotor_multiply = operator_multiply


def operator_divide(inputs):
    for i, c in enumerate(inputs):

        if c in data['targets'][1]['blocks']:
            values = []
            for v in list(data['targets'][1]['blocks'][c]['inputs'].values()):
                if type(v[1]) == str:
                    values.append(v[1])
                else:
                    values.append(v[1][1])
            inputs[i:1] = parse(data['targets'][1]['blocks']
                                [c]['opcode'], values, values)
    return [inputs[0]+"/"+inputs[1]]


def operator_random(inputs):
    pass


def operator_lt(inputs):
    for i, c in enumerate(inputs):

        if c in data['targets'][1]['blocks']:
            values = []
            for v in list(data['targets'][1]['blocks'][c]['inputs'].values()):
                if type(v[1]) == str:
                    values.append(v[1])
                else:
                    values.append(v[1][1])
            inputs[i:1] = parse(data['targets'][1]['blocks']
                                [c]['opcode'], values, values)
    return [inputs[0]+"<"+inputs[1]]


def operator_equals(inputs):
    for i, c in enumerate(inputs):

        if c in data['targets'][1]['blocks']:
            values = []
            for v in list(data['targets'][1]['blocks'][c]['inputs'].values()):
                if type(v[1]) == str:
                    values.append(v[1])
                else:
                    values.append(v[1][1])
            inputs[i:1] = parse(data['targets'][1]['blocks']
                                [c]['opcode'], values, values)
    return [inputs[0]+"="+inputs[1]]


def operator_gt(inputs):
    for i, c in enumerate(inputs):

        if c in data['targets'][1]['blocks']:
            values = []
            for v in list(data['targets'][1]['blocks'][c]['inputs'].values()):
                if type(v[1]) == str:
                    values.append(v[1])
                else:
                    values.append(v[1][1])
            inputs[i:1] = parse(data['targets'][1]['blocks']
                                [c]['opcode'], values, values)
    return [inputs[0]+">"+inputs[1]]


def operator_and(inputs):
    return inputs


def operator_or(inputs):
    return inputs


def operator_not(inputs):
    return inputs


def flipperoperator_isInBetween(inputs):
    for i, c in enumerate(inputs):

        if c in data['targets'][1]['blocks']:
            values = []
            for v in list(data['targets'][1]['blocks'][c]['inputs'].values()):
                if type(v[1]) == str:
                    values.append(v[1])
                else:
                    values.append(v[1][1])
            inputs[i:1] = parse(data['targets'][1]['blocks']
                                [c]['opcode'], values, values)
    return [inputs[1]+">="+inputs[0]+">="+inputs[2]]


def operator_join(inputs):
    for i, c in enumerate(inputs):

        if c in data['targets'][1]['blocks']:
            values = []
            for v in list(data['targets'][1]['blocks'][c]['inputs'].values()):
                if type(v[1]) == str:
                    values.append(v[1])
                else:
                    values.append(v[1][1])
            inputs[i:1] = parse(data['targets'][1]['blocks']
                                [c]['opcode'], values, values)
    return ["'"+inputs[0]+"'.join('"+inputs[1]+"')"]


def operator_letter_of(inputs):
    for i, c in enumerate(inputs):

        if c in data['targets'][1]['blocks']:
            values = []
            for v in list(data['targets'][1]['blocks'][c]['inputs'].values()):
                if type(v[1]) == str:
                    values.append(v[1])
                else:
                    values.append(v[1][1])
            inputs[i:1] = parse(data['targets'][1]['blocks']
                                [c]['opcode'], values, values)
    return [inputs[1]+"["+inputs[0]+"]"]


def operator_length(inputs):
    for i, c in enumerate(inputs):

        if c in data['targets'][1]['blocks']:
            values = []
            for v in list(data['targets'][1]['blocks'][c]['inputs'].values()):
                if type(v[1]) == str:
                    values.append(v[1])
                else:
                    values.append(v[1][1])
            inputs[i:1] = parse(data['targets'][1]['blocks']
                                [c]['opcode'], values, values)
    return ["len("+inputs[0]+")"]


def operator_contains(inputs):
    for i, c in enumerate(inputs):
        if c in data['targets'][1]['blocks']:
            values = []
            for v in list(data['targets'][1]['blocks'][c]['inputs'].values()):
                if type(v[1]) == str:
                    values.append(v[1])
                else:
                    values.append(v[1][1])
            inputs[i:1] = parse(data['targets'][1]['blocks']
                                [c]['opcode'], values, values)
    return [inputs[0]+" in "+inputs[1]]


def operator_round(inputs):
    for i, c in enumerate(inputs):
        if c in data['targets'][1]['blocks']:
            values = []
            for v in list(data['targets'][1]['blocks'][c]['inputs'].values()):
                if type(v[1]) == str:
                    values.append(v[1])
                else:
                    values.append(v[1][1])
            inputs[i:1] = parse(data['targets'][1]['blocks']
                                [c]['opcode'], values, values)
    return ["round("+inputs[0]+")"]


def operator_mathop(inputs):
    return inputs


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
    for i, c in enumerate(inputs):
        if c in data['targets'][1]['blocks']:
            values = []
            for v in list(data['targets'][1]['blocks'][c]['inputs'].values()):
                if type(v[1]) == str:
                    values.append(v[1])
                else:
                    values.append(v[1][1])
            for v in list(data['targets'][1]['blocks'][c]['fields'].values()):
                if type(v[1]) == str:
                    values.append(v[0])
                else:
                    values.append(v[0][0])
            inputs[i:1] = parse(data['targets'][1]['blocks']
                                [c]['opcode'], values, values)
    listtypes=['%', 'cm', 'i']
    listfuncs=['motor.get_distance_percentage()', 'motor.get_distance_cm()', 'motor.get_distance_inches()']

    return [listfuncs[listtypes.index(inputs[3])]+inputs[2]+inputs[1]]


def flippersensors_force(inputs):
    for i, c in enumerate(inputs):
        if c in data['targets'][1]['blocks']:
            values = []
            for v in list(data['targets'][1]['blocks'][c]['inputs'].values()):
                if type(v[1]) == str:
                    values.append(v[1])
                else:
                    values.append(v[1][1])
            inputs[i:1] = parse(data['targets'][1]['blocks']
                                [c]['opcode'], values, values)
    return inputs


def flippersensors_isPressed(inputs):
    return ['force.is_pressed()']


def flippersensors_reflectivity(inputs):
    return ['color.get_reflected_light()']


def flippersensors_isReflectivity(inputs):
    for i, c in enumerate(inputs):
        if c in data['targets'][1]['blocks']:
            values = []
            for v in list(data['targets'][1]['blocks'][c]['inputs'].values()):
                if type(v[1]) == str:
                    values.append(v[1])
                else:
                    values.append(v[1][1])
            inputs[i:1] = parse(data['targets'][1]['blocks']
                                [c]['opcode'], values, values)
    return ["color.get_reflected_light()"+inputs[2]+inputs[1]]

def flippersensors_color(inputs):
    return ['color.get_color()']


def flippersensors_isColor(inputs):
    for i, c in enumerate(inputs):
        if c in data['targets'][1]['blocks']:
            values = []
            for v in list(data['targets'][1]['blocks'][c]['inputs'].values()):
                if type(v[1]) == str:
                    values.append(v[1])
                else:
                    values.append(v[1][1])
            inputs[i:1] = parse(data['targets'][1]['blocks']
                                [c]['opcode'], values, values)
    return ["color.get_color()"+inputs[2]+inputs[1]]


def sound_volume(inputs):
    return ['hub.speaker.get_volume()']


def flippermotor_absolutePosition(inputs):
    return ['motor.get_position()']


def flippermotor_speed(inputs):
    return ['motor.get_speed()']


def parse(opcode, inputs, ifnotfind=None):
    try:
        # (eval(f'{opcode}({inputs})'))
        return eval(f'{opcode}({inputs})')
    except NameError:
        return ifnotfind
