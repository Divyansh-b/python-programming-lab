num1=eval(input("Enter the 1st number "))
num2=eval(input("Enter the 2nd number "))
num3=eval(input("Enter the 3rdvnumber "))

if num1 > num2:
    if num1 > num3:
        print(f"{num1} is maximum")
    else:
        print(f"{num3} is maximum")
elif num1 < num2:
    if num2 > num3:
        print(f"{num2} is maximum")
    else:
        print(f"{num3} is maximum")

                 #or

print(max(num1,num2,num3))
