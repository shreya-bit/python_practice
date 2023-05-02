a=0
b=1
c=2
n=int(input("enter n: "))
print(a)
print(b)
print(c)
for i in range(2,n):
    d=a+b+c
    print(d)
    a=b
    b=c
    c=d


