def read_input(filename):
    with open(filename, 'r') as f:
        data = f.read()
    return data

def parse_input(data):
    r = data.split(',')
    return [int(val) for val in r]

def _get_value(values, parameter, mode):
    if mode == 'P':
        return values[parameter]
    elif mode == 'I':
        return parameter
    else:
        raise Exception("Invalid mode: {}".format(mode))

OP_CODE_TO_INST_LENGTH = {
    1: 4,
    2: 4,
    3: 2,
    4: 2,
    5: 3,
    6: 3,
    7: 4,
    8: 4,
    99: 1,
}

class Instruction(object):
    def __init__(self, input):
        self.op_code = input % 100
        self.parameter_modes = ['P'] * 3
        self.length = OP_CODE_TO_INST_LENGTH[self.op_code]

        input /= 100
        curr_param = 0
        while input > 0:
            mode = input % 10
            self.parameter_modes[curr_param] = 'P' if mode == 0 else 'I'
            input /= 10
            curr_param += 1

    def get_param_value(self, values, parameters, index):
        return _get_value(values, parameters[index], self.parameter_modes[index])

    def perform(self, values, parameters, input, pointer):
        if self.op_code in (1,2,5,6,7,8):
            v1 = self.get_param_value(values, parameters, 0)
            v2 = self.get_param_value(values, parameters, 1)

        if self.op_code == 1 or self.op_code == 2:
            assert self.parameter_modes[2] == 'P'
            values[parameters[2]] = v1 + v2 if self.op_code == 1 else v1 * v2
        elif self.op_code == 3:
            values[parameters[0]] = input
        elif self.op_code == 4:
            print(self.get_param_value(values, parameters, 0))
        elif self.op_code == 5 or self.op_code == 6:
            if (self.op_code == 5 and v1 != 0) or (self.op_code == 6 and v1 == 0):
                return v2
        elif self.op_code == 7:
            v3 = 1 if v1 < v2 else 0
            values[parameters[2]] = v3
        elif self.op_code == 8:
            v3 = 1 if v1 == v2 else 0
            values[parameters[2]] = v3

        return pointer + self.length


def run(values, input):
    pointer = 0
    while True:
        instruction = Instruction(values[pointer])
        if instruction.op_code == 99:
            break
        
        pointer = instruction.perform(values, values[pointer+1:pointer+instruction.length], input, pointer)
        
    return "Done"

INPUT = 5
print(run(parse_input(read_input('./INPUT')), INPUT))