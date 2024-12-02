# read sample.txt into 2d list "reports"
reports = []
with open("input.txt") as f:
    for line in f:
        reports.append(list(map(int, line.split())))

# Part 1: Determine whether reports are safe
def is_safe_strict(report):
    is_increasing = report[0] < report[1]
    multiplier = 1 if is_increasing else -1
    for i in range(1, len(report)):
        delta = (report[i] - report[i-1]) * multiplier
        if not (1 <= delta <= 3):
            return False
    return True

def is_safe_rec(report, prev, is_increasing):
    if not report:
        return True
    delta = (report[0] - prev) * (1 if is_increasing else -1)
    if not (1 <= delta <= 3):
        return False
    return is_safe_rec(report[1:], report[0], is_increasing)


safe_reports = [report for report in reports if is_safe_rec(report[1:], report[0], report[0] < report[1])]
print(f"Part 1: Safe Reports = {len(safe_reports)}")

# Part 2: can leave out one number from each report

def is_safe_soft(report):
    if is_safe_strict(report[1:]):
        return True

    for i in range(1, len(report)):
        if is_safe_strict(report[:i] + report[i+1:]):
            return True

    return False

safe_reports = [report for report in reports if is_safe_soft(report)]
print(f"Part 2: Safe Reports = {len(safe_reports)}")





