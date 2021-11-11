p = int(10/2)+1

start = range(1, p)
st = 1

for i in start :
    p-=1
    o = p-1
    print(" "*o, end="")
    print("*"*st)
    st+=2

p=0
o=0
st-=2
for i in start :
    print(" "*o, end="")
    o=p+1
    p+=1
    print("*"*st)
    st-=2