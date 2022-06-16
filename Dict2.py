# generate number and print a dictionary

n=int(input("Input a number : "))
d = dict()  # function to create a dict
d1=dict()
for x in range(1,n+1):
    d[x]=x*x
    d1[x]=x*x*x

print(d)
print(d1)
