text = open("input21.txt", 'r').read()
text = open("input21test.txt", 'r').read()

import textwrap
from functools import cache

graph = {
    "A^": "<",
    "A<": "v<<",
    "Av": "v<",
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
    "vA": ">^",
    "v<": "<",
    "v>": ">",
    "vv": "",

    ">^": "<^",
    ">A": "^",
    "><": "<<",
    ">v": "<",
    ">>": "",
}

# def process_string_as_parts(string, part_len=200):
#     outstr = ""
#     parts = textwrap.wrap(string, part_len)
#     curpos = "A"
#     for i,part in enumerate(parts):
#         outstr += process(part, curpos=curpos)
#         curpos = part[-1]
#     return outstr

def process_string_as_parts(string):
    outstr = ""
    parts = string.split("A")
    curpos = "A"
    for i,part in enumerate(parts):
        if i != len(parts) - 1:
            part = part + "A"
        outstr += process(part, curpos=curpos)
        curpos = curpos if not len(part) else part[-1]
    return outstr

@cache
def process(string, curpos="A"):
    totals = []
    newstring = ""
    for c in string:
        newstring += graph[curpos + c] + "A"
        curpos = c
    return newstring

def do_part(part):

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
            for k in range(2):
                newstring = process_string_as_parts(newstring)
            totals.append(n * len(newstring))

        return sum(totals)

    else:

        totals = []
        for n,string in strings:
            newstring = string
            for k in range(15):
                newstring = process_string_as_parts(newstring)
            totals.append(n * len(newstring))

        return sum(totals)


import time
start = time.perf_counter()
print(do_part(1))
print(f"Execution time: {time.perf_counter() - start:.4f} seconds")

start = time.perf_counter()
print(do_part(2))
print(f"Execution time: {time.perf_counter() - start:.4f} seconds")
