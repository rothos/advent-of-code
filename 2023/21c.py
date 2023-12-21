
def ccn(n): return 2*n*(n+1)+1
def cccn(n): return ccn(n) - ccn(n-1)
N = 26501365
cccn(N)


# ((202300*2 + 1)**2 / 9) * 34009
# 618593363395201 (wrong)


# from math import floor,ceil

# inner = 3797
# nine = 34009
# twentyfive = 94353
# eightyone = 305437

# # a*41 + b*40 = 305437
# # a*13 + b*12 = 94353
# inner = 27219/7; outer = 25552/7

# N = (26501365 - 65) // 131
# x = (N*2 + 1)**2
# ans = ceil(x/2)*inner + floor(x/2)*outer
# print(ans)
# # 617051186907688.5
# # 617051186907689 (wrong)


# i*5 + o*4 = 34009
# i*13 + o*12 = 94353
#
# i = (34009 - o*4)/5
# o = (94353-i*13)/12
#
# i = (34009 - (94353-i*13)/12*4)/5
# i = 3837


# inner = 3797
# nine = 34009
# outer = (nine - 5*inner) // 4
# N = (26501365 - 65) // 131
# N = 2
# x = (N*2 + 1)**2
# err = -40*N
# err = 0
# ans = ceil(x/2)*inner + floor(x/2)*outer + err
# print(ans)
# # 618220486687597 orig (wrong)
# # 618220478595597 error term (wrong)


# twentyfive = 94353
# nine = 34009
# inner = 3797
# outer = (twentyfive - 13*inner) / 12

# N = (26501365 - 65) // 131
# x = (N*2 + 1)**2

# ans = ceil(x/2)*inner + floor(x/2)*outer
# print(ans)
# # 617674813456930.4
# # 617674813456930 (wrong)
