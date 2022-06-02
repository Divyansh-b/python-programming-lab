list1 = eval(input())
list2 = []
list3 = []
str1 = ""
str2 = ""
n = int(input())
x = int(input())
l = len(list1)
for i in range(n, l):
    a = list1[i]
    if a != ' ':
        str1 = str1+a+' '
for j in range(0, n):
    b = list1[j]
    if b != ' ':
        str2 = str2+b+' '
print((str1+str2)*x)

