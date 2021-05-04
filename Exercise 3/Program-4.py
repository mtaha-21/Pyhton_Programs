# 4. Write a python program to input 5 subject marks and calculate total marks, percentage and grade based on following criteria
# i)percentage less than 50 (Grade C)
# ii)percentage equal to 50 and less than 80 (Grade B)
# iii)percentage equal to 80 and more than 80 (Grade A)


for i in range (6):
     sub[i]=int(input("Enter marks of subject:",i))


sub1=int(input("Enter marks of the first subject: "))
sub2=int(input("Enter marks of the second subject: "))
sub3=int(input("Enter marks of the third subject: "))
sub4=int(input("Enter marks of the fourth subject: "))
sub5=int(input("Enter marks of the fifth subject: "))
avg=(sub1+sub2+sub3+sub4+sub5)/5
if(avg>=80):
    print("Grade: A")
elif(avg>=50&avg<80):
    print("Grade: B")
elif(avg>=30&avg<50):
    print("Grade: C")
else:
    print("Grade: F")