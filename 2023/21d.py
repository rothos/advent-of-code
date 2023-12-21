file = "input21.txt"
# file = "input21-lawrence.txt"
# file = "test21.txt"

from math import floor, ceil

with open(file, 'r') as f:
    content = f.read()
    grid = [list(l) for l in content.split("\n")]

i_odd = 0
i_even = 0
o_odd = 0
o_even = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '#':
            if abs(i-65)+abs(j-65) < 64:
                # inner
                if (i+j) % 2 == 0:
                    i_even += 1
                else:
                    i_odd += 1
            else:
                # outer
                if (i+j) % 2 == 0:
                    o_even += 1
                else:
                    o_odd += 1

# print("i_odd ", i_odd)   # 558
# print("i_even", i_even)  # 505
# print("o_odd ", o_odd)   # 523
# print("o_even", o_even)  # 503
# i_odd  = 558
# i_even = 505
# o_odd  = 523
# o_even = 503

# i_odd  += 1
# i_even += 3
# o_odd  += 2

# x = (65+131+1)**2 - i_even - 4*i_odd - (o_odd+o_even)*2
# # print(x)

done = False
for a in range(5):
    for b in range(5):
        for c in range(5):
            i_odd2 = i_odd + a
            i_even2 = i_even + b
            o_odd2 = o_odd + c

            N = 26501365
            N = 65 + 131*4

            total = (N+1)**2

            megasteps = (N - 65) // 131
            megatiles = (megasteps*2 + 1)**2

            splits = floor(megatiles/2)
            wholes = ceil(megatiles/2)

            odds = (megasteps + 1)**2
            evens = megasteps**2

            rocks = odds*i_odd2 + evens*i_even2 + splits*(o_odd2+o_even)/2

            ans = total - rocks
            # print(ans)

            if ans == 305437:
                print(a,b,c)
                done = True
                break
        if done: break
    if done: break


i_odd  += a
i_even += b
o_odd  += c

N = 26501365

total = (N+1)**2

megasteps = (N - 65) // 131
megatiles = (megasteps*2 + 1)**2

splits = floor(megatiles/2)
wholes = ceil(megatiles/2)

odds = (megasteps + 1)**2
evens = megasteps**2

rocks = odds*i_odd + evens*i_even + splits*(o_odd+o_even)/2

ans = total - rocks
print(ans)



# LAWRENCE
# i_odd 569
# i_even 476
# o_odd 501
# o_even 536
