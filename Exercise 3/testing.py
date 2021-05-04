sub = [None] * 5
for i in range (6):
    sub[i]=input("Enter marks of subject")
    print (i)
totalmarks=sum(sub)
average=totalmarks/5
print("The average is ", average)
print("The total marks is", totalmarks)


