from collections import Counter

list1, list2 = [], []


def get_lines_as_list(file):
    with open(file) as f:
        return f.read().splitlines()


for line in get_lines_as_list('input.txt'):
    elem1, elem2 = line.split()
    list1.append(int(elem1))
    list2.append(int(elem2))

assert len(list1) == len(list2)

n = len(list1)

list1.sort()
list2.sort()

sol1 = 0

for i in range(n):
    abs_diff = abs(list1[i] - list2[i])
    sol1 += abs_diff

# print(res) # p1 sol

# part2
sol2 = 0

counter2 = Counter(list2)

print(counter2)

for elem1 in list1:
    print(elem1)
    sol2 += elem1 * counter2[elem1]

print('sol2', sol2)

