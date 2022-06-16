def sdmit(name,sal):
    pf=sal*20/100;
    hra=sal*30/100;
    print("Name : " , name ,"\nSalary : " ,sal,"PF : ", pf , "HRA : " ,
          hra , "Total sal : " ,(sal+pf+hra));
    


no=int(input("Enter No : "))
for i in range(no): 
    name=input("Enter Name : ")
    sal=int(input("Enter Salary  : "))
    sdmit(name,sal)
