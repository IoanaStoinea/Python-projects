"""""
n=12345
p=1
m=0
k=0
while n!=0:
    x=25
    i=k
    while i!=0:
        x = int(x/10)
        i-=1
    if x==0:
        c=n%10
    else:
        c=x%10
    m=c*p+m
    n=int(n/10)
    p=p*10
    k+=1
print("M=",m)
print(2%10)
"""""
n=2592
nr=0
c=9
while c>=0:
    m=n
    while m!=0 and m%10!=c:
        m=int(m/10)
    if m!=0:
        nr=nr*10+m%10
    c=c-1
print("nr=", nr)















