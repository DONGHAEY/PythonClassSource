leng = 10
stars = range(1, 6)
s = leng -2

for i in stars :
    print("*"*i, end="")
    print(" "*s, end="")
    print("*"*i, end="")
    print("\n", end="")
    s-=2

s = 0
for i in stars:
    s+=2
    v=leng-s
    v=int(v/2)
    print("*"*v, end="")
    print(" "*s, end="")
    print("*"*v, end="")
    print("\n", end="")