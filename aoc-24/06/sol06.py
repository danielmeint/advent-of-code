INPUT_FILE = 'input.txt'

# read input into 2d array map
direction_to_velocity = {
    '^': (-1, 0),
    '>': (0, 1),
    'v': (1, 0),
    '<': (0, -1)
}

direction_order = ['^', '>', 'v', '<']


def get_area(file_name=INPUT_FILE):
    with open(file_name) as f:
        return [list(line.strip()) for line in f]


area = get_area()
curr_pos = (0, 0)

curr_direction = ''
curr_vel = ()



def print_map():
    for row in area:
        print(''.join(row))


print_map()

# Part 1
ROWS = len(area)
COLS = len(area[0])

# determine curr_pos an curr_vel
for i in range(ROWS):
    for j in range(COLS):
        if area[i][j] in direction_to_velocity:
            curr_pos = (i, j)
            curr_direction = area[i][j]
            curr_vel = direction_to_velocity[area[i][j]]
            break

print(curr_pos, curr_vel)


def mark_visited(coords):
    r, c = coords
    area[r][c] = 'X'


def update_velocity(old_vel):
    global curr_direction
    global curr_vel
    curr_direction_index = direction_order.index(curr_direction)
    next_direction = direction_order[(curr_direction_index + 1) % 4]
    curr_direction = next_direction
    # return direction_to_velocity[next_direction]
    curr_vel = direction_to_velocity[next_direction]


def is_out_of_bounds(next_pos):
    r, c = next_pos
    return not (
            0 <= r < ROWS and
            0 <= c < COLS
    )


def is_obstacle(next_pos):
    r, c = next_pos
    return area[r][c] == '#'


while True:
    mark_visited(curr_pos)
    # calc next_pos and break if out of pounds
    cur_r, cur_c = curr_pos
    vel_r, vel_c = curr_vel
    next_pos = (cur_r + vel_r, cur_c + vel_c)
    if is_out_of_bounds(next_pos):
        print(f'{next_pos} is oob')
        break
    if is_obstacle(next_pos):
        print(f'{next_pos} is obstacle')
        update_velocity(curr_vel)
        print(f'updating velocity to {curr_vel}')
        # break
        continue
    # update position
    print(f'moving to {next_pos}')
    curr_pos = next_pos

print_map()

res = sum(
    sum(1 for cell in row if cell == 'X')
    for row in area
)

print(res)
