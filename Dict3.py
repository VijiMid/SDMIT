
no=int(input("Enter No : "))

d1={}
for i in range(no):
    print()
    name =input("Enter the Name :")
    sal =int(input("Enter the Salary :"))
    d1.update({name : sal })

print(d1)
