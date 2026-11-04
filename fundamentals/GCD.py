# Read two integers from the user
n1=int(input("Enter a number: "))
n2=int(input("Enter another number:"))

# Check the smaller number and search downward for the first common divisor
if n2>=n1:
    for i in range(n1,0,-1):
        if n2%i==0 and n1%i==0:
            # Print and stop at the greatest common divisor
            print("The GCD is={}".format(i))
            break
else:
    for i in range(n2,0,-1):
        if n2%i==0 and n1%i==0:
            # Print and stop at the greatest common divisor
            print("The GCD is={}".format(i))
            break
