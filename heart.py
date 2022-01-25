for i in range(0,6):
    for j in range(0,6+1):
        if (i==0 and j%3!=0) or (i==1 and j%3==0) or (i-j==2) or (i+j==8):
            print("*",end="")
        else:
            print(" ",end="")
    print()
# ***************************************************

n=int(input("Enter the Number:"))
n1=n//2
for i in range(n1,0,-1):
    for j in range(0,i-1):
        print(" ",end="")
    for k in range(0,n1-i+1):
        print("* ",end="")
    if n%2==0:
        for j in range(0,2*(i-1)):
            print(" ",end="")
    else:     #for odd
        for j in range(0,2*(i-1)+2):
            print(" ",end="")
    for k in range(0,n1-i+1):
        print("* ",end="")
    print()
for i in range(0,n):
    for j in range(0,i):
        print(" ",end="")
    for k in range(0,n-i):
        print("* ",end="")
    print()

