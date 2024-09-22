
n,s,k=map(int, input().split())
total = 0
for i in range (n):
    p , q = map(int,input().split())
    total+=( p *q)
    
if  s  >  total :
    total += k
print(total)