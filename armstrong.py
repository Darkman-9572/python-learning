a=int(input("num"))
d1=a%10
d2_=a//10
d2=d2_%10
d3=a//100
s=str(a)
l=len(s)
if (d1**l + d2**l +d3**l)==a:
    print("armstrong")
else:
    print("not")
