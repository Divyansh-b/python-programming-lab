n=int(input())
dict1=eval(input())
dict2={}
dict2=[map(str,raw_input().split()) for x in range(n)]
for i in range(n):
    
    key1=input()
    if key1 in dict1:
        print(dict1.get(key1))
    else:
        print("not found")
