import math

def read_input(filename):
    with open(filename, 'r') as f:
        data = f.read()
    return data

def parse_input(data):
    r = data.split('\n')
    return [int(val) for val in r]

def run(input):
    fuel = 0
    for module_mass in input:
        target_mass = module_mass
        while target_mass:
            fuel_to_add = math.floor(target_mass / 3) - 2
            if fuel_to_add > 0:
                fuel += fuel_to_add
                target_mass = fuel_to_add
            else:
                break

    return fuel

print(run(parse_input(read_input('./INPUT'))))