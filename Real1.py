# List Functions (len, sort, reverse, pop, remove)

no=int(input("Enter No : "))
Li=[]

for x in range(1,(no+1)):
    Li.append(input("Enter the Name"))    
print(Li)

print("Sort List : ")
Li.sort()
print(Li)

for x in range(0,len(Li)): 
    Li[x]=Li[x]+ "-" + input("Enter the Department")

print(Li) 






