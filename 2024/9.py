text = open("input9.txt", 'r').read()
# text = open("input9test.txt", 'r').read()

import copy

def make_disk(diskmap):
    disk = []
    i = 0
    for n in diskmap:
        if i % 2:
            disk += int(n) * [None]
        else:
            disk += int(n) * [i//2]
        i += 1
    return disk

def do_one_swap(disk):
    e = disk.index(None)
    k = len(disk) - 1
    while disk[k] == None:
        k -= 1
    if e < k:
        disk[k], disk[e] = disk[e], disk[k]
    return disk

def draw_disk(disk):
    locs = sorted(disk.keys())
    s = ""
    for loc in locs:
        c = str(disk[loc]['id']) if disk[loc]['id'] != None else '.'
        s += c * disk[loc]['len']
    return s

def move_files_and_get_sum(diskmap):
    diskmap = map(int, diskmap)
    disk = dict()
    location = 0
    for i,n in enumerate(diskmap):
        disk[location] = {'id': i//2 if i%2==0 else None, 'len': n}
        location += n

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

    # do the sum
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

def get_sum(disk):
    disk = copy.deepcopy([d for d in disk if d != None])
    return sum([i*n for i,n in enumerate(disk)])

def day9(text, part2=False):
    diskmap = list(text.strip())
    if not part2:
        disk = make_disk(diskmap)
        while disk.copy() != do_one_swap(disk):
            disk = do_one_swap(disk)
            return get_sum(disk)
    else:
        return move_files_and_get_sum(diskmap)



print(day9(text))
# print(day9(text, part2=True))