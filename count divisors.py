
l=int(input("l"))
r=int(input("r"))
k=int(input("k"))

count=0
for i in range(l,r+1):
    if(i%k==0):
       count+=1
print(count)
