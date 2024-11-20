n=int(input("n: "))
a=0
b=1
c=0

while c<n:
    print(a)
    nth=a+b
    a=b

    b=nth
    c+=1
    
