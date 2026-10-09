row=int(input("Enter number of rows:"))
col=int(input("Enter number of columns:"))
for i in range(1,row+1):
    for j in range(i):
        print(chr(ord("A")+j),end=" ")
    print()