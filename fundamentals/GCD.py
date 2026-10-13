# Read two integers from the user
n1 = int(input("Enter a number: "))
n2 = int(input("Enter another number:"))

# Determine the smaller number to iterate downward from
# The first common divisor found from the end is the GCD
if n2 >= n1:
    for i in range(n1, 0, -1):
        if n2 % i == 0 and n1 % i == 0:
            print("The GCD is={}".format(i))
            break
else:
    for i in range(n2, 0, -1):
        if n2 % i == 0 and n1 % i == 0:
            print("The GCD is={}".format(i))
            break

