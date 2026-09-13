user_input=(input("Enter numbers seperated by spaces:"))
number=[int(num) for num in user_input.split()]
even_sum=0

for num in number:
    if num%2==0:
     even_sum+=num

print("Sum of even numbers=",even_sum)