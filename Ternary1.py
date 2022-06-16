a =int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))

# Ternary
print("a is big" if (a>b) else "b is big" if (b > c) else "c is big"  if (c>a) else "a is big" )
