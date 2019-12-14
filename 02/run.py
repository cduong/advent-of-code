import math

def read_input(filename):
    with open(filename, 'r') as f:
        data = f.read()
    return data

def parse_input(data):
    r = data.split(',')
    return [int(val) for val in r]

TARGET = 19690720

def run(values):
    original = list(values)
    found_n, found_v = -1, -1

    for n in range(100):
        for v in range(100):
            values = list(original)
            values[1], values[2] = n, v
            curr_pos = 0
            while True:
                op_code = values[curr_pos]
                
                if op_code == 99:
                    break

                val1, val2 = values[values[curr_pos+1]], values[values[curr_pos+2]]
                if op_code == 1:
                    res = val1 + val2
                elif op_code == 2:
                    res = val1 * val2
                else:
                    raise Exception("Error. Opcode {} at pos {}".format(op_code, curr_pos))
                
                values[values[curr_pos+3]] = res
                curr_pos += 4

            if values[0] == TARGET:
                found_n, found_v = n, v
                break
            
        if found_n != -1:
            break
            
    return 100 * n + v

print(run(parse_input(read_input('./INPUT'))))