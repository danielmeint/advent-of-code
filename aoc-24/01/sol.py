# Read input
with open("input.txt") as f:
    left, right = zip(*(map(int, line.split()) for line in f))

# Part 1: Calculate total distance
sorted_left = sorted(left)
sorted_right = sorted(right)
total_distance = sum(abs(a - b) for a, b in zip(sorted_left, sorted_right))
print(f"Part 1: Total Distance = {total_distance}")

# Part 2: Calculate similarity score
from collections import Counter

right_count = Counter(right)
similarity_score = sum(num * right_count[num] for num in left)
print(f"Part 2: Similarity Score = {similarity_score}")
