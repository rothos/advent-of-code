test = 0
data = open('p10%s.txt' % ('','test')[test], 'r').readlines()
data = [l.strip() for l in data]

def reverse_bracket(c):
    if c == "{": return "}"
    if c == "(": return ")"
    if c == "<": return ">"
    if c == "[": return "]"
    if c == "}": return "{"
    if c == ")": return "("
    if c == ">": return "<"
    if c == "]": return "["

# part 1

scores = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

total = 0
for line in data:
    stack = []
    for c in line:
        if c in "{[(<":
            stack.append(c)
        elif reverse_bracket(c) == stack.pop():
            # valid closing character
            continue
        else:
            # corrupted line
            total += scores[c]
            break

print(total)


# part 2

from functools import reduce

scores = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}

totals = []
for line in data:
    stack = []
    corrupted = False
    for c in line:
        if c in "{[(<":
            stack.append(c)
        elif reverse_bracket(c) == stack.pop():
            # valid closing character
            continue
        else:
            # corrupted line, discard
            corrupted = True
            break
    
    if not corrupted:
        seq = list(map(reverse_bracket, stack))[::-1]
        score = reduce(lambda total,c: total*5 + scores[c], seq, 0)
        totals += [score]

totals = sorted(totals)
print(totals[len(totals)//2])
