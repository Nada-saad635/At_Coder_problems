n = int(input())
nums = list(map(int,input().split()))
leng= len(nums)
b = " "
for i in range(leng-1):
    a = nums[i]*nums[i+1]
    b += str(a)
print(b)    
