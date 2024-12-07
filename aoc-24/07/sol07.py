INPUT_FILE = 'input.txt'

# read into lines
lines = []
with open(INPUT_FILE) as f:
    for line in f:
        lines.append(line.strip())

targets = []
constants = []

for line in lines:
    res, nums = line.split(':')
    res = int(res)
    nums = [int(x) for x in nums.split()]
    targets.append(res)
    constants.append(nums)  # don't sort, order is important, dou

# memo = {}

print(targets)
print(constants)


# recursive
def can_cut(target, param):
    if target < param:
        return False
    return str(target).endswith(str(param))

assert can_cut(156, 6)
assert can_cut(123, 23)
assert not can_cut(123, 4)

def cut_off(target, param):
    if target == param:
        return 0
    print(target, param)
    param_str = str(param)
    target_str = str(target)
    cut_target_str = target_str[:-len(param_str)]
    return int(cut_target_str)

# Tests
assert cut_off(156, 6) == 15, "oops"
assert cut_off(123, 23) == 1, "oops2"

def can_match(target, nums, allow_pipe):
    # print(f'can_match({target}, {nums}, {allow_pipe})')

    if not nums:
        return (
                target == 0 or  # sum?
                target == 1  # multiplication?
        )
    if len(nums) == 1:
        return target == nums[0]
    if target < min(nums):
        return False
    return (
            can_match(target - nums[-1], nums[:-1], allow_pipe) or
            (
                    target % nums[-1] == 0 and
                    can_match(target // nums[-1], nums[:-1], allow_pipe)
            ) or
            # pipe
            (
                    allow_pipe and
                    can_cut(target, nums[-1]) and
                    can_match(cut_off(target, nums[-1]), nums[:-1], allow_pipe)
            )

    )


# Part 1
res = sum(targets[i] for i in range(len(targets)) if can_match(targets[i], constants[i], allow_pipe=False))

print(f'Part 1: {res}')

# Part 2
res = sum(targets[i] for i in range(len(targets)) if can_match(targets[i], constants[i], allow_pipe=True))

print(f'Part 2: {res}')
