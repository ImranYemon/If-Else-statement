Marks =int(input("enter your marks :"))

if (Marks<=100 and Marks>=80):
    gread= "A+"
elif (Marks<80 and Marks>=70):
    gread= "A"
elif (Marks<70 and Marks>=60):
    gread= "A-"
elif (Marks<60 and Marks>=50):
    gread= "B"
elif (Marks<50 and Marks>=40):
    gread= "C"
else:
    gread= "F"

print(gread)
