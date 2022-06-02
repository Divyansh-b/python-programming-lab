n = int(input())
list1 = []
list2 = []
list3 = []
for i in range(n):
    name = input()
    score = eval(input())
    list1.append(name)
    list2.append(score)
list3 = list2.copy()
a = min(list2)
list2.delete(a)
b = (min(list2))
for j in range(1,n+1):
    x = (list3[j-1])
    if x == b:
        y = list1[j-1]
        print(y)
    else:
        print(x)
print(list1)
print(list2)
print(list3)
print(x)
print(y)
