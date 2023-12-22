from math import prod, floor, ceil
from collections import Counter, defaultdict
from itertools import permutations, combinations
import re
from functools import cache
from copy import deepcopy as copy

import time
time0 = time.time()

# We want to turn the string
#    "px{a<2006:qkq,m>2090:A,rfg}"
# into the tuple
#    ("px", [("a", (1,2005), "qkq"), ("m", (2091,4001), True), "rfg"])
def parseworkflow(s):
    name, rules = s.split("{")
    rules = rules[:-1].split(",")
    rules = [parserule(rule) for rule in rules]
    return (name, rules)

# Turns the string "a<2006:qkq" into the tuple ("a", (1,2005), "qkq")
# and the string "rfg" into the string "rfg"
def parserule(s):
    if len(s.split(":")) == 1:
        return s

    cond,res = s.split(":")

    if "<" in cond:
        param, num = cond.split("<")
        interval = (1,int(num))
    else:
        param, num = cond.split(">")
        interval = (int(num)+1,4001)

    return (param, interval, res)

def get_overlap(ruleinterval, myinterval):
    a, b = max(ruleinterval[0],myinterval[0]), min(ruleinterval[1],myinterval[1])
    overlap = (a,b) if a<b else None
    if overlap == None:
        rest = myinterval
    elif overlap == myinterval:
        rest = None
    else:
        if overlap[0] == myinterval[0]:
            rest = (overlap[1], myinterval[1])
        else:
            rest = (myinterval[0], overlap[0])
    
    return overlap, rest

def recurse(name, params):
    if name == "R":
        return 0
    if name == "A":
        return prod([(x[1]-x[0]) for x in params.values()])

    rules = workflows[name]
    ans = 0
    for rule in rules:
        if type(rule) == str:
            ans += recurse(rule, copy(params))
        else:
            xmas,ruleinterval,outname = rule
            myinterval = params[xmas]
            overlap,rest = get_overlap(ruleinterval,myinterval)
            if overlap:
                params[xmas] = overlap
                ans += recurse(outname, copy(params))
                params[xmas] = rest

    return ans


file = "input19.txt"
# file = "test19.txt"

with open(file, 'r') as f:
    content = f.read()
    workflows = dict()
    for workflow in content.split("\n\n")[0].split("\n"):
        name, rules = parseworkflow(workflow)
        workflows[name] = rules

total = recurse("in", {"x":(1,4001), "m":(1,4001), "a":(1,4001), "s":(1,4001)})
print(total)


time1 = time.time()
print("-- %.3fs --" % (time1-time0))
