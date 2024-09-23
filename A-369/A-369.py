a , b = map(int, input().split())
x = 0
if b-a == 0 :
    x = 1
elif(b - a) % 2 == 0 :
    x = 3
elif ( b -a) % 2 != 0 :
    x = 2
print(x)    
