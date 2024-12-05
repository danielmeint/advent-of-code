from collections import defaultdict

INPUT_FILE = "input.txt"

# read into lines
lines = []
with open(INPUT_FILE) as f:
    for line in f:
        lines.append(line.strip())

successors = defaultdict(set)
predecessors = defaultdict(set)

updates = []


def parse_rule(rule):
    # split by |
    parts = [int(x) for x in rule.split("|")]
    assert len(parts) == 2, f"Invalid rule: {rule}"
    # print(f'Rule: {parts[0]} | {parts[1]}')
    successors[parts[0]].add(parts[1])
    predecessors[parts[1]].add(parts[0])


for line in lines:
    if not line:
        break
    parse_rule(line)

# parse updates
for line in lines:
    if ',' not in line:
        continue
    updates.append([int(x) for x in line.split(",")])


def is_valid_update(update):
    seen = set()
    for elem in update:
        must_come_after = successors[elem]
        if any(seen_elem in must_come_after for seen_elem in seen):
            return False
        seen.add(elem)
    return True


def get_middle_page_number(update):
    return update[len(update) // 2]


res = sum(
    get_middle_page_number(update) if is_valid_update(update) else 0 for update in updates
)
print(f'Part 1: {res}')

### Part 2

incorrect_updates = [
    update for update in updates if not is_valid_update(update)
]


def correct_update(update):
    remaining_elems = set(update)
    res = []

    def find_next_elem():
        def can_be_first(elem):
            return not (any(other_elem in predecessors[elem] for other_elem in remaining_elems))

        for elem in remaining_elems:
            if can_be_first(elem):
                return elem

    while remaining_elems:
        next_elem = find_next_elem()
        remaining_elems.remove(next_elem)
        res.append(next_elem)
    return res


corrected_updates = [
    correct_update(update) for update in incorrect_updates
]

res = sum(
    get_middle_page_number(u) for u in corrected_updates
)

print(f'Part 2: {res}')
