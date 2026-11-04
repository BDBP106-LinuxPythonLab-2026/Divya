#1
# n = int(input("enter a number: "))
# if n > 0:
#     print(n, "is positive")
#     if n % 2 == 0:
#         print(n, "is even")
#     else:
#         print(n, "is odd")
# if n < 0:
#     print(n, "is negative")
#     if n % 2 == 0:
#         print(n, "is even")
#     else:
#         print(n, "is odd")
# if n % 3 == 0 and n % 5 == 0:
#     print(n, "Fizzbuzz number")
# else:
#     print(n, "is zero")

#2
# def count_sentences(sentence):
#     vowels = set('aeiouAEIOU')
#     consonants = set('bcdfghjklmnpqrstvwxyz')
#     digits = set('0123456789')
#     space = set(' ')
# 
#     vowel_count = 0
#     cons_count = 0
#     digit_count = 0
#     space_count = 0
#     
#     for char in sentence:
#         if char in vowels:
#             vowel_count += 1
#         if char in consonants:
#             cons_count += 1
#         if char in digits:
#             digit_count += 1
#         if char in space:
#             space_count += 1
#     return vowel_count , cons_count, digit_count, space_count
# text = input('Enter a sentence: ')
# print (count_sentences(text))

#3
# x = 25
# count_attp = 0
# for i in range(1,50):
#      g = int(input("Guess a number between 1 and 50: "))
#      count_attp += 1
#      if g == x:
#          print("you guessed right")
#          print("number of attempts",count_attp)
#          break
#      elif g > x:
#          print("your number is too high ")
#          print("number of attempts",count_attp)
# 
#      elif g < x:
#          print("your number is too low")
#          print("number of attempts",count_attp)
#      if count_attp == 7:
#          print("the secret number is",x)
#          break

#6
n = [("Asha", 88), ("Ravi", 72), ("Meera", 95), ("Karan", 59), ("Divya", 81)]
t = 
for n in range (1,11):
    if n >= 90:
        print("A")
    if n >= 80:
        print("B")
    if n >= 70:
        print("C")
    if n >= 60:
        print("D")
    else :
        print("F")    

    
        
            
