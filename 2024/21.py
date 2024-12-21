text = open("input21.txt", 'r').read()
text = open("input21test.txt", 'r').read()

graph = {
    "A^": "<",
    "A<": "v<<",
    "Av": "v<",
    "A>": "v",

    "^A": ">",
    "^<": "v<",
    "^v": "v",
    "^>": "v>",

    "<^": ">^",
    "<A": ">>^",
    "<v": ">",
    "<>": ">>",

    "v^": "^",
    "vA": ">^",
    "v<": "<",
    "v>": ">",

    ">^": "<^",
    ">A": "^",
    "><": "<<",
    ">v": "<",
}

def process(string):
    totals = []
    newstring = ""
    curpos = "A"
    for c in string:
        if curpos == c:
            newstring += "A"
        else:
            newstring += graph[curpos + c] + "A"
        curpos = c
    return newstring



def do_part(part):

    if part == 1:
        strings = [
            # (29, "<A^A>^^AvvvA"),
            # (980, "^^^A<AvvvA>A"),
            # (179, "^<<A^^A>>AvvvA"),
            # (456, "^^<<A>A>AvvA"),
            # (379, "^A<<^^A>>AvvvA"),

            (208, "<^AvA^^^Avvv>A"),
            (540, "<^^A<A>vvA>A"),
            (685, "^^A<^AvAvv>A"),
            (879, "<^^^A<A>>AvvvA"),
            (826, "<^^^AvvA^>AvvA")
        ]

        totals = []
        for n,string in strings:
            newstring = process(process(string))
            print(len(newstring), process(string), newstring)
            totals.append(n * len(newstring))

        print(totals, sum(totals))

    else:
        pass


import time
start = time.perf_counter()
print(do_part(1))
# 615366
# 237458
# 222166
# 224326
print(f"Execution time: {time.perf_counter() - start:.4f} seconds")

start = time.perf_counter()
print(do_part(2))
print(f"Execution time: {time.perf_counter() - start:.4f} seconds")
