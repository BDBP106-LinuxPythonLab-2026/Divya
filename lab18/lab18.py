#1
# D = dict( [ ('apple','red'), ('grapes','green') ] )
# for k,v in D.items():
#     print(k,v)

#2
# D = dict(a=1, b=2, c=3)
# total = sum(D.values())
# print(total)
#     
#3
# D = dict(a=1, b=2, c=3)
# val_max = max(D.values())
# val_min = min(D.values())
# print("MAXIMUM:", val_max, "MINIMUM:", val_min)

#4 remove duplictaes..count length of all keys..check in between the keys
# test_dict= {"Gfg":[5,7,7,7,7], "is":[6,7,7,7], "Best":[9,9,6,5,5]}
# max_count=0
# for key in test_dict:
#     unique=set(test_dict[key])
#     count=len(unique)
#     if count>max_count:
#         max_count=count
#         max_key=key
# print(max_key)


#5 str to list to dict
# sentence=input("Enter a sentence")
# words=sentence.split()
# unique_words=set(words)
# result = []
# for word in unique_words:
#     result.append(word)
# 

#5 only using dict



#6
# def function_area():
#     import math
#     a = 1
#     b = 2
#     c = 3
#     s = (a + b + c) // 2
#     area = math.sqrt(s*(s - a)*(s - b)*(s - c))
#     print(area)
# function_area()   

#7
# def function_area():
#     a = 1
#     b = 2
#     c = 3
#     if a == b == c:
#         print("equilateral")
#     elif a == b != c:
#         print("isosceles")
#     elif a != c != b:    
#         print("scalene")
# function_area()  

#9 first position
# DNA = "AGTCTTATATCT"
# for i in range(0,len(DNA),3):
#     print(DNA[i:i+3])

#9 third position
# DNA = "AGTCTTATATCT"
# for i in range(2,len(DNA),3):
#      print(DNA[i:i+3])
        
# 10 for even and odd
# def function_even(n):
#     if n % 2 == 0:
#         print("Even")
#         n = n + 2
#     else:
#         print("Odd")
#         n = n + 1 
# n = int(input("Enter a number: "))
# function_even(n)  

#10
# def function_prime(n):
    
#8
