INPUT_FILE = 'sample.txt'

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
initial_pos = (0, 0)
curr_pos = (0, 0)

initial_direction = ''
curr_direction = ''


def print_map():
    for row in area:
        print(''.join(row))


print_map()

# Part 1
ROWS = len(area)
COLS = len(area[0])

# determine curr_pos an curr_direction
for i in range(ROWS):
    for j in range(COLS):
        if area[i][j] in direction_to_velocity:
            initial_pos = curr_pos = (i, j)
            initial_direction = curr_direction = area[i][j]
            break


def mark_visited(coords):
    r, c = coords
    area[r][c] = 'X'

def next_direction(direction):
    direction_index = direction_order.index(direction)
    return direction_order[(direction_index + 1) % 4]



def update_direction():
    global curr_direction
    curr_direction = next_direction(curr_direction)


def is_out_of_bounds(next_pos):
    r, c = next_pos
    return not (
            0 <= r < ROWS and
            0 <= c < COLS
    )


def is_obstacle(next_pos):
    r, c = next_pos
    return area[r][c] == '#'

obstacles_to_place = 0


def should_next_be_obstacle():
    # next_pos should be obstacle if current row has a obstacle "to the right" that has a path "on my side" AND in the correct direction
    r_pos_curr, c_pos_curr = curr_pos
    r_vel, c_vel = direction_to_velocity[curr_direction]
    r_pos_next, c_pos_next = r_pos_curr + r_vel, c_pos_curr + c_vel









    return False


while True:
    mark_visited(curr_pos)
    # calc next_pos and break if out of pounds
    cur_r, cur_c = curr_pos
    vel_r, vel_c = direction_to_velocity[curr_direction]
    next_pos = (cur_r + vel_r, cur_c + vel_c)
    if is_out_of_bounds(next_pos):
        print(f'{next_pos} is oob')
        break
    if is_obstacle(next_pos):
        print(f'{next_pos} is obstacle')
        update_direction()
        print(f'updating direction to {curr_direction}')
        # break
        continue
    if should_next_be_obstacle():
        # part 2
        obstacles_to_place += 1
    # update position
    print(f'moving to {next_pos}')
    curr_pos = next_pos

print_map()

res = sum(
    sum(1 for cell in row if cell == 'X')
    for row in area
)

print(f'Part 1: {res}')

# Part 2
# reset area and curr_pos
area = get_area()
curr_pos = initial_pos
curr_direction = initial_direction

number_of_possibilities = 0

print_map()
print(curr_pos, curr_direction)

def mark_with_direction():
    r, c = curr_pos
    area[r][c] = curr_direction

# idea: mark "hit" obstacles and then check if there is one in the row/col
# also need to mark FROM WHICH DIRECTION the obstacle was hit

# doesnt work

# new idea: mark "hit" obstacles; if there is a path on "current side" and going in the correct direction, that's when a loo p is possible



