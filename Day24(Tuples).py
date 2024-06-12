t1=(1,2,76,342,32,"green",True)
t2=(1)
t3=(1,)
# t1[0]=90
print(type(t1),t1)
print(len(t1))
print(t1[0])
print(t1[1])
print(t1[2])

if 342 in t1:
    print("Yes")
else:
    print("No")

t4=t1[1:4]
print(t4)