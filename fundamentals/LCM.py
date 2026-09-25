n1 = int(input("Enter a number: "))
n2 = int(input("Enter another number: "))

gcd = 1
for i in range(min(n1, n2), 0, -1):
    if n1 % i == 0 and n2 % i == 0:
        gcd = i
        break

lcm = (n1 * n2) // gcd

print("The LCM is={}".format(lcm))  
