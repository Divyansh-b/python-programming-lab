list1=eval(input())
list2=[]
list3=[]
for i in list1:
    if i==0:
        list3.append(i)
    else:
        list2.append(i)
print(list2+list3)
