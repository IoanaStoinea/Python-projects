"""""
n=12
d=1
s=0
while (d*d)<n:
    if n%d==0 and (d%2)!=int(n/d)%2:
        s = s+d+int(n/d)
    d=d+1 #d+=1
if (d*d)==n:
    s=s+d
print(s)

n=2
k=3
for i in range(1,n):
    for j in range(k,1,-1):
        print(j, " ")
    for j in range(1,k):
        print(j, " ")
    k=k-1
"""""
x=3
y=12
i=x
j=y
s=0
while i<=j:
    if i%2 == 0:
        s=s+j
    if j%2==0:
        s=s+i
    i=i+1
    j=j-1
print(s)
