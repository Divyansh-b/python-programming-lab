print("Enter the Number: ")
a= int(input())

f = open(r"C:\xampp\htdocs\utkarsh\filehandling_names.txt", 'w')

if f.closed:
    print("file successfully opened")
else:
    print("file not opened")

for i in range(a):
    print(f'Enter the name {i+1}')
    name  = input()
    f.write(name+"\n")

f.close()
if f.closed:
    print("file successfully opened")
else:
    print("file does not opened")
