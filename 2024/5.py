text = open("input5.txt", 'r').read()
# text = open("input5test.txt", 'r').read()


### PART 1

def check_update(u,rules):
    for rule in rules:
        if rule[0] in u and rule[1] in u:
            u1,u2 = ",".join(u).split(rule[0])
            if rule[1] in u1:
                return False
    return True

rules,updates = text.split("\n\n")
rules = [r.split("|") for r in rules.split("\n")]
updates = [u.split(",") for u in updates.split("\n")]

# rules = [[int(r) for r in rule.split("|")] for rule in rules.split("\n")]
# updates = [[int(u) for u in update.split(",")] for update in updates.split("\n")]

total = 0
for u in updates:
    if check_update(u, rules):
        total += int(u[len(u)//2])

print(total)


### PART 2

def fix_update(u,rules):
    borked = False

    for rule in rules:
        if rule[0] in u and rule[1] in u:
            u1,u2 = ",".join(u).split(rule[0])
            if rule[1] in u1:
                borked = True
                a,b = u.index(rule[0]), u.index(rule[1])
                u[a],u[b] = u[b],u[a]

    if not borked:
        return False

    # Uhh just do a bunch of passes i guess
    for _ in range(4):
        for rule in rules:
            if rule[0] in u and rule[1] in u:
                u1,u2 = ",".join(u).split(rule[0])
                if rule[1] in u1:
                    borked = True
                    a,b = u.index(rule[0]), u.index(rule[1])
                    u[a],u[b] = u[b],u[a]

    return u

total = 0
for u in updates:
    if u2 := fix_update(u, rules):
        total += int(u[len(u)//2])

print(total)
