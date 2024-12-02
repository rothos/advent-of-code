file = "input2.txt"
# file = "input2test.txt"

with open(file, 'r') as f:
    lines = f.read()


### PART 1

def safe(nn):
    dd = [nn[i] - nn[i+1] for i in range(len(nn)-1)]
    return all(d>0 and 0<abs(d)<4 for d in dd) or all(d<0 and 0<abs(d)<4 for d in dd)

reps = [[int(n) for n in l.split()] for l in lines.split('\n')]
safes = [safe(r) for r in reps]
print(sum(safes))


### PART 2

def can_make_safe(nn):
    if safe(nn):
        return True
    for i in range(len(nn)):
        nn2 = nn[0:i] + nn[i+1:]
        if safe(nn2):
            return True
    return False

safes = [can_make_safe(r) for r in reps]
print(sum(safes))
