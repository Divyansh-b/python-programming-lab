#2. Program to input the centre of a circle, radius of the circle and an arbitrary point P(x,y) and 
#determine whether the point is inside the circle, on the circle or outside the circle

x1=int(input("enter center of circle x1:"))
x2=int(input("and x2:"))
y1=int(input("enter a arbitrary point y1:"))
y2=int(input("and y2:"))

r=int(input("enter radius of circle: "))

d=(((x1-y1)**2) + ((x2-y2)**2))**0.5

if r==d:
    print("point in circle line.")

elif d>r:
    print("point is outside of circle")

else:
    print("point is inside in the circle.") 
