a=input("str")
b=input("char")
for i in a:
    if i==b:
        print(a.index(b))
    else:
        print("not found")
