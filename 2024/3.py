file = "input3.txt"
# file = "input3test.txt"
text = open(file, 'r').read()

import re

def process(text):
    matches = re.findall(r"mul\(([0-9]+),([0-9]+)\)", text)
    return sum(int(x[0])*int(x[1]) for x in matches)

### PART 1
print(process(text))

### PART 2
dotext = "".join( "".join(t.split("do()")[1:]) for t in ("do()" + text).split("don't()") )
print(process(dotext))
