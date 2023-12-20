from collections import defaultdict

file = "input20.txt"
# file = "test20b.txt"
# file = "test20.txt"

### PART 1

with open(file, 'r') as f:
    content = f.read()
    lines = [l for l in content.split("\n")]


machine = defaultdict(lambda: None)

for line in lines:

    outputs = line.split(" -> ")[1].split(", ")
    name = line.split(" -> ")[0][1:]

    # Broadcaster
    if line[0] == "b":
        machine["broadcaster"] = {
            "type": "broadcaster",
            "outputs": outputs
        }

    if line[0] == "%":
        machine[name] = {
            "type": "flipflop",
            "outputs": outputs,
            "state": False
        }

    if line[0] == "&":
        machine[name] = {
            "type": "conjunction",
            "outputs": outputs,
            "lasts": dict()
        }

for k in machine.keys():
    if machine[k]["type"] == "conjunction":
        for j in machine.keys():
            if k in machine[j]["outputs"]:
                machine[k]["lasts"][j] = False

lows = 0
highs = 0

def go():
    global lows, highs

    # broadcaster receives a low pulse
    pulses = [{"to": "broadcaster", "degree": False, "from": "button"}]

    while len(pulses):

        pulse = pulses.pop(0)

        pulsefrom = pulse["from"]
        pulseto = pulse["to"]
        pulsedegree = pulse["degree"]

        # x = "high" if pulsedegree else "low"
        # print(pulsefrom, "-%s>" % x, name)

        if pulsedegree:
            highs += 1
        else:
            lows += 1

        if machine[pulseto] == None:
            continue

        if machine[pulseto]["type"] == "broadcaster":
            outpulsedegree = pulsedegree

        elif machine[pulseto]["type"] == "flipflop":
            if pulsedegree:
                continue
            else:
                machine[pulseto]["state"] = not machine[pulseto]["state"]
                outpulsedegree = machine[pulseto]["state"]

        elif machine[pulseto]["type"] == "conjunction":
            machine[pulseto]["lasts"][pulsefrom] = pulsedegree
            outpulsedegree = not all(machine[pulseto]["lasts"].values())

        # Queue up new pulses
        for out in machine[pulseto]["outputs"]:
            pulses.append({
                "to": out,
                "degree": outpulsedegree,
                "from": pulseto
                })


for k in range(1000):
    go()

print(lows * highs)
