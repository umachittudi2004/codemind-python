a=int(input()) 

s=0 

t=a 
rev=0 
while(a!=0):
    r=a%10 
    rev=rev*10+r 
    a=a//10 
if(rev==t):
    print("True") 
else: 
    print("False")