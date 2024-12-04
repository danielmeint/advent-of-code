# read sample.txt into 2d list letters
FILE_NAME = "input.txt"

letters = []
with open(FILE_NAME) as f:
    for line in f:
        letters.append(list(line.strip()))

ROWS = len(letters)
COLS = len(letters[0])

print(letters)

DIRECTION_OFFSETS = [
    (-1, -1),  # up left
    (-1, 0),   # up
    (-1, 1),   # up right
    (0, -1),   # left
    (0, 1),    # right
    (1, -1),   # down left
    (1, 0),    # down
    (1, 1)     # down right
]


def matches(from_coords, direction_offset, remaining_word="XMAS"):
    row, col = from_coords
    if not 0 <= row < ROWS or not 0 <= col < COLS:
        return False
    curr_char = letters[row][col]
    first_char = remaining_word[0]
    if curr_char != first_char:
        return False
    if len(remaining_word) == 1:
        return True
    row_offset, col_offset = direction_offset
    new_coords = (row + row_offset, col + col_offset)
    return matches(new_coords, direction_offset, remaining_word=remaining_word[1:])

def count_matches(coords):
    res = 0
    for dir_offset in DIRECTION_OFFSETS:
        if matches(coords, dir_offset):
            res += 1

    print(f'{res} matches from {coords}')
    return res


# res = 0
# for r in range(ROWS):
#     for c in range(COLS):
#         coords = (r, c)
#         res += count_matches(coords)
#
# print(f"Part 1: {res}")
#
### Part 2


def is_xmas_center(coords):
    row, col = coords
    if letters[row][col] != 'A':
        return False
    first_candidate = letters[row-1][col-1] + letters[row+1][col+1]
    second_candidate = letters[row-1][col+1] + letters[row+1][col-1]
    return is_ms(first_candidate) and is_ms(second_candidate)


def is_ms(candidate):
    return candidate == 'MS' or candidate == 'SM'

res = 0
for r in range(1, ROWS-1):
    for c in range(1, COLS-1):
        coords = (r, c)
        if is_xmas_center(coords):
            res += 1


print(f'Part 2: {res}')



