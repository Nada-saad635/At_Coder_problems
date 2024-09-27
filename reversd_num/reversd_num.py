# n = input()
# my_list = []
# i = len(n)

# while i > 0 :
#     my_list.append(n[i-1])

#     i -=1
# print("".join(my_list))

# n = input()
# total = 0
# for i in n :
#     total += int(i)
# print(total)    
 
n= int(input())
total = 0
while n > 0 :
  last = n % 10
  total = total*10 +last
  n = n // 10
  

print(total)


    


