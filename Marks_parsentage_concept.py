# Input from user for marks 
marks1= int(input("entre your marks 1 : "))
marks2= int(input("entre your marks 2 : "))
marks3= int(input("entre your marks 3 : "))

# total_parsentage calculate 
total_parsentage= ((marks1+marks2+marks3)/300)*100 
print(total_parsentage)

if (total_parsentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("Congratulation ! You are passed .") 
else:
    print("sorry , you are failed try aging next year .")