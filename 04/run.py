def read_input(filename):
    with open(filename, 'r') as f:
        data = f.read()
    return data

def parse_input(data):
    range_ = data.split('-')
    return int(range_[0]), int(range_[1])

def _digits_repeat_exactly_twice(digits):
    repeat_lengths = []
    for i in range(len(digits)):
        if i == 0:
            curr_repeat = 1
            continue

        if digits[i] == digits[i-1]:
            curr_repeat += 1
        else:
            repeat_lengths.append(curr_repeat)
            curr_repeat = 1
    return 2 in repeat_lengths

def _is_valid_password(pw):
    digits = []
    while pw > 0:
        digits.append(pw % 10)
        pw /= 10

    # reverse so digits is from left to right
    digits.reverse()
    digits_increase = all([digits[i] <= digits[i+1] for i in range(0, len(digits) - 1)])
    return digits_increase and _digits_repeat_exactly_twice(digits)

def run(range_):
    pw_start, pw_end = range_
    valid_passwords = []
    for pw in range(pw_start, pw_end):
        if _is_valid_password(pw):
            valid_passwords.append(pw)

    return len(valid_passwords)

print(run(parse_input(read_input('./INPUT'))))