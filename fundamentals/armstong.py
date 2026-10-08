num=int(input("Enter a number:"))
temp=num
if num == 0:
    print("Enter valid number")
else:
    sum=0
    power=len(str(num))
    for d in str(num):
        lastdigit=num%10
        num=num//10
        sum=sum+lastdigit**power 
    if temp==sum:
        print(f"{temp} is an armstrong number")
    else:
        print(f"{temp} is not an armstrong number")
       

