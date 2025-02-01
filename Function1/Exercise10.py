def unique(mylist):
    result = []
    for i in mylist:
        if mylist.count(i) == 1:
            result.append(i)
    return result

n = int(input("N: "))
mylist = []
for i in range(n):
    number = int(input("Number: "))
    mylist.append(number)
print(unique(mylist))