def read_input(filename):
    with open(filename, 'r') as f:
        data = f.read()
    return data

def parse_input(data):
    rows = data.split('\n')
    assert len(rows) == 2
    return [
        r.split(",") for r in rows
    ]

# instruction to dx, dy
INSTRUCTION_MAP = {  
    'U': (0, 1),
    'D': (0, -1),
    'L': (-1, 0),
    'R': (1, 0),
}

def _advance_wire(steps_by_coordinate, source, step_no, instruction):
    dir_, dist = instruction[0], int(instruction[1:])
    if dist <= 0:
        raise Exception("Invalid distance: {}".format(instruction))

    curr_coord = source
    direction_delta = INSTRUCTION_MAP[dir_]
    for _ in range(0, dist):
        next_coord = (curr_coord[0] + direction_delta[0], curr_coord[1] + direction_delta[1])
        step_no += 1
        if next_coord not in steps_by_coordinate:
            # only track the shortest distance
            steps_by_coordinate[next_coord] = step_no
        curr_coord = next_coord
    
    return curr_coord, step_no
            
def run(directions):
    wire_locations = []
    for iset in directions:
        source = (0,0)  # 0,0 doesn't count as overlap initially
        steps_by_coordinate = dict()
        steps = 0
        for i in iset:
            dest, steps = _advance_wire(steps_by_coordinate, source, steps, i)
            source = dest
        wire_locations.append(steps_by_coordinate)
    
    crosses = set(wire_locations[0].keys()).intersection(
       set(wire_locations[1].keys()))
    steps = [wire_locations[0][c] + wire_locations[1][c] for c in crosses]
    return min(steps)

print(run(parse_input(read_input('./INPUT'))))