text = open("input21.txt", 'r').read()
# text = open("input21test.txt", 'r').read()

graph = {
    "A^": "<",
    "A<": "v<<",
    "Av": "<v",
    "A>": "v",
    "AA": "",

    "^A": ">",
    "^<": "v<",
    "^v": "v",
    "^>": "v>",
    "^^": "",

    "<^": ">^",
    "<A": ">>^",
    "<v": ">",
    "<>": ">>",
    "<<": "",

    "v^": "^",
    "vA": "^>",
    "v<": "<",
    "v>": ">",
    "vv": "",

    ">^": "<^",
    ">A": "^",
    "><": "<<",
    ">v": "<",
    ">>": "",
}

def process(string, curpos="A"):
    totals = []
    newstring = ""
    for c in string:
        newstring += graph[curpos + c] + "A"
        curpos = c
    return newstring

def zeros(d):
    out = d.copy()
    for key in out:
        out[key] = 0
    return out

def string_to_pairs(string):
    return [string[i:i+2] for i in range(len(string)-1)]

def get_complexity(string, num_robots):
    # freqs = {
    #     "AA": 0, # "A",
    #     "A^": 0, # "<A",
    #     "A<": 0, # "v<<A",
    #     "Av": 0, # "<vA",
    #     "A>": 0, # "vA",
    #     "^A": 0, # ">A",
    #     "^>": 0, # "v>A",
    #     "<^": 0, # ">^A",
    #     "<A": 0, # ">>^A",
    #     "vA": 0, # "^>A",
    #     ">^": 0, # "<^A",
    #     ">A": 0, # "^A",
    # }

    freqs =  {
        "A^": 0,
        "A<": 0,
        "Av": 0,
        "A>": 0,
        "AA": 0,
        "^A": 0,
        "^<": 0,
        "^v": 0,
        "^>": 0,
        "^^": 0,
        "<^": 0,
        "<A": 0,
        "<v": 0,
        "<>": 0,
        "<<": 0,
        "v^": 0,
        "vA": 0,
        "v<": 0,
        "v>": 0,
        "vv": 0,
        ">^": 0,
        ">A": 0,
        "><": 0,
        ">v": 0,
        ">>": 0,
    }


    def map_to_freq_table(ab):
        if ab in freqs: return ab
        elif ab in ['^^', '>>', '<<', 'vv']: return 'AA'
        elif ab in ['v<', '>v']: return 'A^'
        elif ab in ['<v', 'v>']: return '^A'
        elif ab in ['^<']: return '>^'
        print('error 1856')
        return None

    # Convert string to freqs
    for pair in string_to_pairs(string):
        freqs[pair] += 1

    print(freqs)

    # Loop through the robots
    for _ in range(num_robots):
        nums, types = freqs.values(), freqs.keys()
        newfreqs = zeros(freqs)
        for type in freqs:
            if freqs[type]:
                for outtype in string_to_pairs(graph[type] + "A"):
                    newfreqs[outtype] += freqs[type]

        freqs = newfreqs

    print(freqs)
    return sum(freqs[k] for k in freqs.keys()) + 1

def do_part(part):

    strings = [
        (208, "<^AvA^^^Avvv>A"),
        # (540, "<^^A<A>vvA>A"),
        # (685, "^^A<^AvAvv>A"),
        # (879, "<^^^A<A>>AvvvA"),
        # (826, "<^^^AvvA^>AvvA")
    ]

    if part == 1:

        totals = []
        for n,string in strings:
            newstring = string
            totals.append(n * len(process(process(string))))
            # totals.append(n * len(string))

        return sum(totals)

    else:

        totals = []
        for n,string in strings:
            newstring = string
            print(get_complexity(string, 1))
            totals.append(n * get_complexity(string, 1))

        print(string)
        print(process(string))

        return sum(totals)



import time
# start = time.perf_counter()
# print(do_part(1))
# print(f"Execution time: {time.perf_counter() - start:.4f} seconds")

start = time.perf_counter()
print(do_part(2))
# 151659080102 too low
print(f"Execution time: {time.perf_counter() - start:.4f} seconds")
