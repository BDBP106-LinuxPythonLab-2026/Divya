#1
# L = [1,1,0,1]
# decimal = 0
# power = 0
# L = L.reverse()
# for i in range(0,len(L)):

#3
# n = int(input("enter a number "))
# if n <= 1:
#     return False
# for i in range(2, int(n**0.5)+1):
#     if n % i == 0:
#         print(i)
#         break


#4
# n = str(input("enter a number" ))
# for i in range(0,len(n)):
#     print(n[i])

#5
# n = str(input("enter a number"))
# for i in range(len(n)//2):
#     print(n[i])

#6
# n = str(input("enter a number : "))
# for i in range(0,len(n),2):
#     print(n[i])

#8
# n = str(input("enter a string: "))
# n.count("W")
# print(n.count("W"))

#10
# L = [2,5,89,88,4,34,83,7]
# for i in range(len(L)):
#     if L[i] % 2 == 0:
#         print( L[i],"even")

#11
# L = [1, 2, 3, 2, 4, 5, 1, 6, 1, 7, 5]
#
# seen = set()
# duplicates = set()
#
# for element in L:
#     if element in seen:
#         duplicates.add(element)
#     else:
#         seen.add(element)
# print("Duplicate elements:", list(duplicates))


#15
# L = ["kite","lamp","pineapple","koala"]
# for i in L:
#     if i.startswith("k"):
#         print(i)

#14
# L = [34,376,5,2,4,3,3,3,3,3,3,3,3]
# L2 = L.copy()
# n = int(input("Enter a number to remove in L : "))
# 
# for x in L:
#     if n == x:
#         L2.remove(x)
# print(L2)

#13
L = [34,376,5,2,4,3,3,3,3,3,3,3,3]
for i in L:
    if L.count(3) > 2:
print(i)
        
        




