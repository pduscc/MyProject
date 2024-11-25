x = [3,4,0,2,1,8,-1]
n=0
s=0
m=0
a=0

while x[n] != -1:
    s+=x[n]
    
    if m>x[n]:
        m=x[n]
    n+=1

a = s/n

print (n,s,m,a)

# it looks like I learned how to use git today