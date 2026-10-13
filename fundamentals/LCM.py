# Read two numbers from the user
n1 = int(input("Enter a number: "))
n2 = int(input("Enter another number: "))

# Find the greatest common divisor (GCD) using a loop
# Starting from the smaller number and moving downward
# The first number that divides both values evenly is the GCD
gcd = 1
for i in range(min(n1, n2), 0, -1):
    if n1 % i == 0 and n2 % i == 0:
        gcd = i
        break

# Calculate the LCM using the formula: LCM = (a * b) / GCD
lcm = (n1 * n2) // gcd

# Display the result
print("The LCM is={}".format(lcm))
