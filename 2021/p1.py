
# part 1

nn = open('p1.txt','r').readlines()
nn = map(int, nn)
# nn = [199,200,208,210,200,207,240,269,260,263]
diffs = map(lambda i:nn[i+1]-nn[i], range(len(nn)-1))
count = len(filter(lambda x:x>0, diffs))
print(count)


# part 2

sums = map(lambda i:sum(nn[i:i+3]), range(len(nn)-2))
diffs2 = map(lambda i:sums[i+1]-sums[i], range(len(sums)-1))
count2 = len(filter(lambda x:x>0, diffs2))
print(count2)
