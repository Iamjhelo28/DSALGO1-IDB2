factorList=[]
x = int(input("Enter a number: "))
for i in range (1, x+1):
    if x % i ==0:
        factorList.append(i)
print("The factors of ",x, " are: ", factorList)
