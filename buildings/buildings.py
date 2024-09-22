num = int(input())
buldings = list(map(int,input().split()))
taller =-1 
for i in range(num-1):
    if buldings[0] < buldings[i+1]:
        taller = i +2
print(taller)        