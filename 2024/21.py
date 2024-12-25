text = open("input21.txt", 'r').read()
# text = open("input21test.txt", 'r').read()

from functools import lru_cache

graph = {
    "A^": "<A",
    "A<": "v<<A",
    "Av": "<vA",
    "A>": "vA",
    "AA": "A",

    "^A": ">A",
    "^<": "v<A",
    "^v": "vA",
    "^>": "v>A",
    "^^": "A",

    "<^": ">^A",
    "<A": ">>^A",
    "<v": ">A",
    "<>": ">>A",
    "<<": "A",

    "v^": "^A",
    "vA": "^>A",
    "v<": "<A",
    "v>": ">A",
    "vv": "A",

    ">^": "<^A",
    ">A": "^A",
    "><": "<<A",
    ">v": "<A",
    ">>": "A",
}

def process(string, curpos="A"):
    totals = []
    newstring = ""
    for c in string:
        newstring += graph[curpos + c]
        curpos = c
    return newstring

def do_part(part):

    # I did the first round by hand (directions for numeric keypad)
    strings = [
        (208, "<^AvA^^^Avvv>A"),
        (540, "<^^A<A>vvA>A"),
        (685, "^^A<^AvAvv>A"),
        (879, "<^^^A<A>>AvvvA"),
        (826, "<^^^AvvA^>AvvA")
    ]

    if part == 1:

        totals = []
        for n,string in strings:
            newstring = string
            totals.append(n * len(process(process(string))))

        return sum(totals)

    else:

        @lru_cache(maxsize=None)
        def count_length(string, num_robots):
            if num_robots == 0:
                return len(string)

            prev = 'A'
            total = 0
            for c in string:
                total += count_length(graph[prev + c], num_robots-1)
                prev = c

            return total

        totals = []
        for n,string in strings:
            newstring = string
            totals.append(n * count_length(string, 25))

        return sum(totals)


import time
start = time.perf_counter()
print(do_part(1))
print(f"Execution time: {time.perf_counter() - start:.4f} seconds")

start = time.perf_counter()
print(do_part(2))
print(f"Execution time: {time.perf_counter() - start:.4f} seconds")
