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
            newstring = string
            for k in range(2):
                newstring = process(newstring)
            # newstring = process(process(string))
            # print(len(newstring), process(string), newstring)
            totals.append(n * len(newstring))

        print(totals, sum(totals))

    else:
        pass


import time
start = time.perf_counter()
print(do_part(1))
# 615366 wrong
# 237458 wrong
# 222166 wrong
# 224326 right!!
print(f"Execution time: {time.perf_counter() - start:.4f} seconds")

start = time.perf_counter()
print(do_part(2))
print(f"Execution time: {time.perf_counter() - start:.4f} seconds")




"""
+---+---+---+
| 7 | 8 | 9 |
+---+---+---+
| 4 | 5 | 6 |
+---+---+---+
| 1 | 2 | 3 |
+---+---+---+
    | 0 | A |
    +---+---+

    +---+---+
    | ^ | A |
+---+---+---+
| < | v | > |
+---+---+---+

029A
<A^A>^^AvvvA

980A
^^^A<AvvvA>A

179A
^<<A^^A>>AvvvA

456A
^^<<A>A>AvvA

379A
^A<<^^A>>AvvvA




208A
<^AvA^^^A>vvvA

540A
<^^A<A>vvA>A

685A
^^A^<AvA>vvA

879A
^^^<A<A>>AvvvA

826A
^^^<AvvA^>AvvA










>A<AAv<AA^>>AvAA^Av<AAA>^A
vA^A<<vA^>>AA<<vA>A>^AA<Av>AA^Av<A>^AA<A>Av<A<A^>>AAAvA<^A>A


>Av<<AA>^AA>AvAA^A<vAAA>^A
vA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A


    +---+---+
    | ^ | A |
+---+---+---+
| < | v | > |
+---+---+---+


<v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A

<A>A<AAv<AA^>>AvAA^Av<AAA>^A
<<vA^>>AvA^A<<vA^>>AA<<vA>A>^AA<Av>AA^Av<A>^AA<A>Av<A<A^>>AAAvA<^A>A

"""
