n=int(input("enter the number to check"))
sum=0
counter=1
num=n
rev=0
while(n>0):
    rev= rev*10 + n%10
    n=n/10

print(rev)
""" extract one digit, then increase a counter"""
while (rev>0):
    dig=rev%10
    sum+=pow(dig,counter)
    counter=counter+1
    rev=rev/10

if(sum==num):
    print("disarium")
else:
    print("boo not disarium")

