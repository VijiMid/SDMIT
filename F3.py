name=[]
sal=[]
def sdmit(name,sal):
    for i in range(0,len(name)): 
        pf=sal[i]*20/100
        hra=sal[i]*30/100;
        print("Name : " , name[i] ,"\nSalary : " ,sal[i],"PF : ", pf , "HRA : " ,
          hra , "Total sal : " ,(sal[i]+pf+hra));    

NaList=[]
SalList=[]
no=int(input("Enter No : "))
for i in range(no): 
    NaList.append(input("Enter Name : "))
    SalList.append(int(input("Enter Salary  : ")))

sdmit(NaList,SalList)
