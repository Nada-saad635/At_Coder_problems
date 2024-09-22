num = int(input())
buldings = list(map(int,input().split()))
taller =-1 
for i in range(1,num):
    if buldings[0] < buldings[i]:
        taller = i +1
        break 
print(taller)        