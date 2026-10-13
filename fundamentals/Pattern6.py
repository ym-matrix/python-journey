n=int(input("Enter no of rows and columns:"))
for i in range(1,n+1):
    space=" "*(n-1)
    for j in range(1,n+1):
        if j<=i:
            print('*')
       
