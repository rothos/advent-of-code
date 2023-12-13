import re
file = "input1.txt"

### PART 1

def linesum1(line):
    x = re.compile(r"\d")
    digits = x.findall(line)
    return int(digits[0])*10 + int(digits[-1])

with open(file, 'r') as f:
    lines = f.readlines()

nn1 = []
for line in lines:
    nn1 += [linesum1(line.strip())]

print(sum(nn1))
# 53194


### PART 2

def linesum2(line):
    a = re.compile(r"^.*?(\d|one|two|three|four|five|six|seven|eight|nine)")
    z = re.compile(r".*(\d|one|two|three|four|five|six|seven|eight|nine).*?$")
    first = a.search(line).group(1)
    last = z.search(line).group(1)
    dicto = {
        "one": 1,   "1": 1,
        "two": 2,   "2": 2,
        "three": 3, "3": 3,
        "four": 4,  "4": 4,
        "five": 5,  "5": 5,
        "six": 6,   "6": 6,
        "seven": 7, "7": 7,
        "eight": 8, "8": 8,
        "nine": 9,  "9": 9
    }
    return dicto[first]*10 + dicto[last]

nn2 = []
for line in lines:
    nn2 += [linesum2(line.strip())]

print(sum(nn2))
# 54249
