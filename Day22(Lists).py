marks=[3,5,6,"Sourav",True,6,7,2,32,345,23]
# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])
# print(marks[4])

# print(marks[-3]) #Negative Index
# print(marks[len(marks)-3]) #Positive Index
# print(marks[5-3]) #Positive Index
# print(marks[2]) #Positive Index

# if 7 in marks:
#     print("Yes")
# else:
#     print("No")
# if "Sourav" in marks:
#     print("Yes")
# else:
#     print("No")
# if "6" in marks:
#     print("Yes")
# else:
#     print("No")

# Same thing applies for strings as well
# if "So" in "Sourav":
#     print("Yes")

# print(marks)
# print(marks[:])
# print(marks[1:])
# print(marks[1:-1]) #5-1=4 therfor 1 to 4
# print(marks[1:8])
# print(marks[1:8:2])

lst=[i for i in range(4)]
print(lst)
lst=[i*i for i in range(10)]
print(lst)
lst=[i for i in range(10) if i%2==0]
print(lst)