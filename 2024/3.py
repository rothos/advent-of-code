file = "input3.txt"
# file = "input3test.txt"

lines = open(file, 'r').read().splitlines()

### PART 1

import re
pattern = re.compile(r"mul\(([0-9]+),([0-9]+)\)")
matches = re.findall(pattern, "".join(lines))
total = sum([int(x[0])*int(x[1]) for x in matches])
print(total)

### PART 2
 
text = ""
for t in ("do()" + "".join(lines)).split("don't()"):
    text += "".join(t.split("do()")[1:])

matches = re.findall(pattern, text)
total = sum([int(x[0])*int(x[1]) for x in matches])
print(total)
