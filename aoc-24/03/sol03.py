# regex to find
import re


def from_file(file):
    with open(file) as f:
        return f.read()


pattern = r'mul\((\d*),(\d*)\)'  # with 2 groups
text = from_file("input.txt")

# Part 1: Calculate sum of multiplication

def calc_sum(text):
    matches = re.findall(pattern, text)

    res = 0
    for match in matches:
        res += int(match[0]) * int(match[1])

    return res

print(f"Part 1: {calc_sum(text)}")

# Part 2

ENABLE_INSTRUCTION = "do()"
DISABLE_INSTRUCTION = "don't()"

res = 0
curr = 0

while curr < len(text):
    # if is_active:
    next_deactivate = text.find(DISABLE_INSTRUCTION, curr)
    next_deactivate = next_deactivate if next_deactivate > 0 else len(text) + 1
    res += calc_sum(text[curr:next_deactivate+1]) #?
    curr = next_deactivate + len(DISABLE_INSTRUCTION)
    if next_deactivate > len(text):
        break
    curr = text.find(ENABLE_INSTRUCTION, curr)
    curr = curr if curr > 0 else len(text) + 1

print(res)








