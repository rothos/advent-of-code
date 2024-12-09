text = open("input9.txt", 'r').read()
# text = open("input9test.txt", 'r').read()


### PART 1

def do_one_swap(disk):
    e = disk.index(None)
    k = len(disk) - 1
    while disk[k] == None:
        k -= 1
    if e < k:
        disk[k], disk[e] = disk[e], disk[k]
    return disk

def get_sum1(disk):
    disk = [d for d in disk if d != None]
    return sum([i*n for i,n in enumerate(disk)])

def do_part1(diskmap):
    disk = []
    i = 0
    for n in diskmap:
        if i % 2:
            disk += int(n) * [None]
        else:
            disk += int(n) * [i//2]
        i += 1

    while disk.copy() != do_one_swap(disk):
        disk = do_one_swap(disk)

    return get_sum1(disk)


### PART 2

# Drawing function for debugging
def draw_disk(disk):
    locs = sorted(disk.keys())
    s = ""
    for loc in locs:
        c = str(disk[loc]['id']) if disk[loc]['id'] != None else '.'
        s += c * disk[loc]['len']
    return s

def make_disk(diskmap):
    disk = dict()
    location = 0
    for i,n in enumerate(diskmap):
        disk[location] = {'id': i//2 if i%2==0 else None, 'len': n}
        location += n
    return disk

def get_sum2(disk):
    total = 0
    for loc in disk.keys():
        file = disk[loc]
        if file['id'] == None:
            continue
        k = 0
        while k < file['len']:
            total += (loc+k)*file['id']
            k += 1
    return total

def do_part2(diskmap):
    disk = make_disk(diskmap)
    locs = sorted(disk.keys())
    filelocs = [l for l in locs if disk[l]['id']]
    for fileloc in filelocs[::-1]:
        for eloc in sorted(disk.keys()):
            if disk[eloc]['id'] == None and disk[eloc]['len'] >= disk[fileloc]['len']:
                if eloc > fileloc:
                    break

                emptylen = disk[eloc]['len']
                filelen = disk[fileloc]['len']
                disk[eloc], disk[fileloc] = disk[fileloc].copy(), disk[eloc].copy()
                if emptylen != filelen:
                    disk[eloc+filelen] = {'id': None, 'len': emptylen - filelen}
                    disk[fileloc]['len'] = filelen

                break

    return get_sum2(disk)



diskmap = list(map(int, list(text.strip())))
print(do_part1(diskmap))
print(do_part2(diskmap))
