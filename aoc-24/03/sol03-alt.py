import re


def sum_enabled_mul(memory: str) -> int:
    # Regex to match valid mul instructions
    mul_regex = re.compile(r"mul\((\d+),(\d+)\)")
    # Regex to match control instructions
    control_regex = re.compile(r"(do\(\)|don't\(\))")

    # Track if mul instructions are enabled
    mul_enabled = True
    total_sum = 0

    # Split the memory by the control instructions while preserving delimiters
    parts = re.split(control_regex, memory)

    for part in parts:
        # Check for control instructions
        if part == "do()":
            mul_enabled = True
        elif part == "don't()":
            mul_enabled = False
        else:
            # Look for valid mul instructions in this section
            for match in mul_regex.finditer(part):
                if mul_enabled:
                    x, y = map(int, match.groups())
                    total_sum += x * y

    return total_sum


# Example Usage
memory = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
result = sum_enabled_mul(memory)
print(result)  # Should output 48
