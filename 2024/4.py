lines = open("input4.txt", 'r').read().splitlines()
# lines = open("input4test.txt", 'r').read().splitlines()

### PART 1

def rotate(m):
    x = list(list(x) for x in zip(*m))[::-1]
    x = ["".join(y) for y in x]
    return x

total = 0
for k in range(4):

    w = len(lines[0])
    h = len(lines)

    for i,line in enumerate(lines):
        for j,char in enumerate(line):
            if char == 'X':
                # E ->
                if j < w-3 and line[j:j+4] == "XMAS":
                    total += 1
                # SE -> v
                if j < w-3 and i < h-3 and lines[i][j]+lines[i+1][j+1]+lines[i+2][j+2]+lines[i+3][j+3] == "XMAS":
                    total += 1

    lines = rotate(lines)

print(total)


### PART 2

total = 0
for k in range(4):

    w = len(lines[0])
    h = len(lines)

    for i,line in enumerate(lines):
        for j,char in enumerate(line):
            if char == 'A':
                if 0 < i < h-1 and 0 < j < w-1 \
                        and lines[i-1][j-1] == "M" and lines[i-1][j+1] == "M" \
                        and lines[i+1][j-1] == "S" and lines[i+1][j+1] == "S":
                    total += 1

    lines = rotate(lines)

print(total)
