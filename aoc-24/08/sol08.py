from collections import defaultdict

import math

FILE_INPUT = 'input.txt'


def read_map(file_name):
    with open(file_name) as f:
        return [list(line.strip()) for line in f]


def print_map(area):
    for row in area:
        print(''.join(row))


area = read_map(FILE_INPUT)
print_map(area)

frequency_to_antennas = defaultdict(set)

ROWS = len(area)
COLS = len(area[0])

for r in range(ROWS):
    for c in range(COLS):
        if area[r][c] != '.':
            frequency_to_antennas[area[r][c]].add((r, c))

print(frequency_to_antennas)

antinodes = set()


def get_delta(a, b):
    return (b[0] - a[0], b[1] - a[1])


# Tests
assert get_delta((0, 0), (1, 1)) == (1, 1)
assert get_delta((0, 0), (1, 0)) == (1, 0)


def calc_antinodes(a, b):
    delta = get_delta(a, b)
    antinode1 = (b[0] + delta[0], b[1] + delta[1])
    antonode2 = (a[0] - delta[0], a[1] - delta[1])
    return antinode1, antonode2


# Tests
assert calc_antinodes((0, 0), (1, 1)) == ((2, 2), (-1, -1)), calc_antinodes((0, 0), (1, 1))


def is_inbounds(point):
    r, c = point
    return (
            0 <= r < ROWS and
            0 <= c < COLS
    )


# Tests
assert is_inbounds((0, 0))
assert is_inbounds((ROWS - 1, COLS - 1))
assert not is_inbounds((ROWS, COLS))
assert not is_inbounds((ROWS - 1, COLS))

all_antinodes = set()

for frequency in frequency_to_antennas:
    antennas = list(frequency_to_antennas[frequency])
    for i in range(len(antennas) - 1):
        for j in range(i + 1, len(antennas)):
            a, b = antennas[i], antennas[j]
            antinodes_pair = calc_antinodes(a, b)
            all_antinodes.update(antinodes_pair)  # add both

valid_antinodes = set(a for a in all_antinodes if is_inbounds(a))
print(f'Part 1: {len(valid_antinodes)}')


## Part 2

def reduce(delta):
    # find the greatest common divisor
    gcd = math.gcd(delta[0], delta[1])
    return delta[0] // gcd, delta[1] // gcd


# Test
assert reduce((2, 2)) == (1, 1)
assert reduce((3, 3)) == (1, 1)
assert reduce((4, 2)) == (2, 1)
assert reduce((4, 3)) == (4, 3)


# def update_by(point, delta):
#     return point[0] + delta[0], point[1] + delta[1]


def calc_all_antinodes(start, delta):
    assert delta != (0, 0), "huh"
    res = set()
    # negative dir
    cur = start
    while (is_inbounds(cur)):
        res.add(cur)
        cur = (cur[0] - delta[0], cur[1] - delta[1])
    # pos dir
    cur = start
    while (is_inbounds(cur)):
        res.add(cur)
        cur = (cur[0] + delta[0], cur[1] + delta[1])

    return res


all_antinodes_2 = set()

for frequency in frequency_to_antennas:
    antennas = list(frequency_to_antennas[frequency])
    for i in range(len(antennas) - 1):
        for j in range(i + 1, len(antennas)):
            a, b = antennas[i], antennas[j]
            delta = get_delta(a, b)
            reduced_delta = reduce(delta)
            antinodes = calc_all_antinodes(a, reduced_delta)
            all_antinodes_2.update(antinodes)

valid_antinodes_2 = set(a for a in all_antinodes_2 if is_inbounds(a))
print(f'Part 2: {len(valid_antinodes_2)}')
