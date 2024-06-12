number=int(input("Enter number:"))
for n in range(0, number + 1):
    flag=0
    if n==0 or n==1:
        flag=1
    else:
        for j in range(2,n-1):
            if(n%j==0):
                flag=1
    if flag==0:
        print(f'{n}',end=' ')






number=int(input("\nEnter number:"))
for n in range(2, number + 1):
    flag=0
    for j in range(2,n-1):
        if(n%j==0):
            flag=1
    if flag==0:
        print(f'{n}',end=' ')