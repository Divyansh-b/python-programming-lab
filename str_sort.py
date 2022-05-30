string = input("Enter the string : ")

strList=list(string) 

sortedString=''.join(sorted(strList, reverse =True)) 
print("String Sorted in ascending order :", sortedString)
