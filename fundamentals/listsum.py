user_input=(input("Enter numbers seperated by spaces:"))
#to split the numbers at the trailing spaces
number=[int(num) for num in user_input.split()]
even_sum=0

for num in number:
# condition to check even 
    if num%2==0:
     even_sum+=num

print("Sum of even numbers=",even_sum)