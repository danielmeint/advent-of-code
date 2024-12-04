# Constants and setup
FILE_NAME = "input.txt"

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

# Load letters into a 2D list
def load_letters(file_name):
    with open(file_name) as f:
        return [list(line.strip()) for line in f]

letters = load_letters(FILE_NAME)
ROWS, COLS = len(letters), len(letters[0])


# Part 1 Functions
def matches(from_coords, direction_offset, remaining_word="XMAS"):
    row, col = from_coords
    if not (0 <= row < ROWS and 0 <= col < COLS):
        return False
    if letters[row][col] != remaining_word[0]:
        return False
    if len(remaining_word) == 1:
        return True

    row_offset, col_offset = direction_offset
    new_coords = (row + row_offset, col + col_offset)
    return matches(new_coords, direction_offset, remaining_word[1:])


def count_matches(coords, word="XMAS"):
    return sum(matches(coords, offset, word) for offset in DIRECTION_OFFSETS)


def part_1():
    total_matches = sum(
        count_matches((r, c))
        for r in range(ROWS)
        for c in range(COLS)
    )
    print(f"Part 1: {total_matches}")


# Part 2 Functions
def is_xmas_center(coords):
    row, col = coords
    if letters[row][col] != 'A':
        return False

    def is_ms(candidate):
        return candidate in {"MS", "SM"}

    diagonal_1 = letters[row - 1][col - 1] + letters[row + 1][col + 1]
    diagonal_2 = letters[row - 1][col + 1] + letters[row + 1][col - 1]
    return is_ms(diagonal_1) and is_ms(diagonal_2)


def part_2():
    total_centers = sum(
        is_xmas_center((r, c))
        for r in range(1, ROWS - 1)
        for c in range(1, COLS - 1)
    )
    print(f"Part 2: {total_centers}")


# Main Execution
if __name__ == "__main__":
    part_1()
    part_2()
