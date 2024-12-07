def parse_input(file_path):
    grid = []
    guard_position = None
    guard_direction = None
    directions = {"^": 0, ">": 1, "v": 2, "<": 3}

    with open(file_path, 'r') as f:
        for y, line in enumerate(f):
            line = line.strip()
            row = []
            for x, char in enumerate(line):
                if char in directions:
                    guard_position = (x, y)
                    guard_direction = directions[char]
                    row.append('.')
                else:
                    row.append(char)
            grid.append(row)

    return grid, guard_position, guard_direction


def turn_right(direction):
    return (direction + 1) % 4


def move_forward(position, direction):
    x, y = position
    if direction == 0:  # Up
        return x, y - 1
    elif direction == 1:  # Right
        return x + 1, y
    elif direction == 2:  # Down
        return x, y + 1
    elif direction == 3:  # Left
        return x - 1, y


def simulate(grid, start_position, start_direction, obstruction=None):
    visited_states = set()
    position = start_position
    direction = start_direction

    while 0 <= position[1] < len(grid) and 0 <= position[0] < len(grid[0]):
        state = (position, direction)
        if state in visited_states:
            return True  # Loop detected
        visited_states.add(state)

        # Check for obstacle
        forward_position = move_forward(position, direction)
        if forward_position == obstruction or (
                0 <= forward_position[1] < len(grid)
                and 0 <= forward_position[0] < len(grid[0])
                and grid[forward_position[1]][forward_position[0]] == "#"
        ):
            direction = turn_right(direction)
        else:
            position = forward_position

    return False  # No loop detected


def count_valid_obstruction_positions(grid, guard_position, guard_direction):
    valid_positions = 0

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "." and (x, y) != guard_position:
                if simulate(grid, guard_position, guard_direction, (x, y)):
                    valid_positions += 1

    return valid_positions


# Main execution
if __name__ == "__main__":
    file_path = "input.txt"  # Make sure this file exists in the same directory as the script
    grid, guard_position, guard_direction = parse_input(file_path)
    result = count_valid_obstruction_positions(grid, guard_position, guard_direction)
    print(f"Number of valid obstruction positions: {result}")
