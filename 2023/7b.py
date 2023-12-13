from collections import Counter

def translate_hand(hand):
    rr = {
        "A": "a",
        "K": "b",
        "Q": "c",
        "T": "e",
        "9": "f",
        "8": "g",
        "7": "h",
        "6": "i",
        "5": "j",
        "4": "k",
        "3": "l",
        "2": "m",
        "J": "n"
    }
    for a,b in rr.items():
        hand = hand.replace(a,b)

    C1 = Counter(hand)
    nJ = C1['n']
    hc = ''
    items = sorted(C1.items(), key=lambda x: str(x[1])+str(500-ord(x[0])), reverse=True)
    # print(items)
    for c,n in items:
        if c != 'n':
            hc = c
            break

    hand2 = hand.replace('n',hc)
    # print(hand,hand2)
    C2 = Counter(hand2)
    cv = sorted(list(C2.values()),reverse=True)

    if cv == [5]: return "A" + hand
    if cv == [4,1]: return "B" + hand
    if cv == [3,2]: return "C" + hand
    if cv == [3,1,1]: return "D" + hand
    if cv == [2,2,1]: return "E" + hand
    if cv == [2,1,1,1]: return "F" + hand
    if cv == [1,1,1,1,1]: return "G" + hand

    return "Annnnn"

with open("input7.txt", "r") as f:
# with open("test7.txt", "r") as f:
    lines = list(f.readlines())
    hands = [x.strip().split(" ") for x in lines]
    # hands = [["2233J","100"]]
    hands = list(map(lambda x: [translate_hand(x[0]), x[1]], hands))
    hands = sorted(hands, key=lambda x:x[0])
    nn = range(len(hands),0,-1)
    total = sum([nn[i]*int(hands[i][1]) for i in range(len(hands))])

print(total)
