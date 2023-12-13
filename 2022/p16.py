from copy import deepcopy

data = open('p16test.txt', 'r').readlines()
data = [l.strip().split(' ') for l in data if l.strip()]
cave = dict([[d[0], [int(d[1]), d[2].split(',')]] for d in data])

paths = [{  'pos': 'AA',
            'opens': [],
            'score': 0,
            'mins': 0
            }]

best = 0

newpaths = []
for path in paths:

    pos = path['pos']
    opens = path['opens']
    score = path['score']
    mins = path['mins']
    flow_rate = cave[pos][0]
    tunnels = cave[pos][1]

    # print(sum([cave[o][0] for o in opens]))
    new_pressure = sum([cave[o][0] for o in opens])

    # if mins >= 30:
    #     print(score)
    #     continue

    for tunnel in tunnels:
        newpaths += [{ 'pos': tunnel,
                    'opens': opens,
                    'score': score+new_pressure,
                    'mins': mins+1
                    }]
        if pos not in opens:
            newpaths += [{ 'pos': tunnel,
                        'opens': opens + [pos],
                        'score': score+new_pressure+flow_rate,
                        'mins': mins+2
                        }]
paths = newpaths

newpaths = []
for path in paths:

    pos = path['pos']
    opens = path['opens']
    score = path['score']
    mins = path['mins']
    flow_rate = cave[pos][0]
    tunnels = cave[pos][1]

    # print(sum([cave[o][0] for o in opens]))
    new_pressure = sum([cave[o][0] for o in opens])

    # if mins >= 30:
    #     print(score)
    #     continue

    for tunnel in tunnels:
        newpaths += [{ 'pos': tunnel,
                    'opens': opens,
                    'score': score+new_pressure,
                    'mins': mins+1
                    }]
        if pos not in opens:
            newpaths += [{ 'pos': tunnel,
                        'opens': opens + [pos],
                        'score': score+new_pressure+flow_rate,
                        'mins': mins+2
                        }]
paths = newpaths

newpaths = []
for path in paths:

    pos = path['pos']
    opens = path['opens']
    score = path['score']
    mins = path['mins']
    flow_rate = cave[pos][0]
    tunnels = cave[pos][1]

    # print(sum([cave[o][0] for o in opens]))
    new_pressure = sum([cave[o][0] for o in opens])

    # if mins >= 30:
    #     print(score)
    #     continue

    for tunnel in tunnels:
        newpaths += [{ 'pos': tunnel,
                    'opens': opens,
                    'score': score+new_pressure,
                    'mins': mins+1
                    }]
        if pos not in opens:
            newpaths += [{ 'pos': tunnel,
                        'opens': opens + [pos],
                        'score': score+new_pressure+flow_rate,
                        'mins': mins+2
                        }]
paths = newpaths
newpaths = []



while paths:

    max_score = -1
    winner = None
    for i,path in enumerate(paths):
        if path['score'] > max_score:
            max_score = path['score']
            winner = i
    path = paths.pop(i)

    pos = path['pos']
    opens = path['opens']
    score = path['score']
    mins = path['mins']
    flow_rate = cave[pos][0]
    tunnels = cave[pos][1]

    # print(sum([cave[o][0] for o in opens]))
    new_pressure = sum([cave[o][0] for o in opens])

    if mins >= 30:
        if score > best:
            best = score
            print(best)
        continue

    for tunnel in tunnels:
        paths += [{ 'pos': tunnel,
                    'opens': opens,
                    'score': score+new_pressure,
                    'mins': mins+1
                    }]
        if pos not in opens:
            paths += [{ 'pos': tunnel,
                        'opens': opens + [pos],
                        'score': score+new_pressure+flow_rate,
                        'mins': mins+2
                        }]

    












# paths = [['AA']]
# paths = [['AA','DD','CC','BB','AA','II','JJ','II','AA','DD','EE','FF','GG','HH','GG','FF','EE','DD','CC']]

# def calc_pressure(path):
#     total_pressure = 0
#     mins = 0

#     visited = []

#     for i in range(len(path)):
#         if mins >= 30:
#             break

#         room = path[i]
#         flow_rate = cave[room][0]
#         #tunnels = cave[room][1]

        
#         if room not in visited and flow_rate > 0:
#             mins += 1
#             total_pressure += flow_rate*(30-mins)

#         visited += [room]
#         mins += 1

#     return total_pressure

# for path in paths:
#     print(','.join(path) + " " + str(int(calc_pressure(path))))
