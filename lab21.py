#1
# celsius = [ 2, 4, 6, 86]
# fahrenheit = map(lambda x: (x * 9) / 5 + 32, celsius)
# print(list(fahrenheit))

#2
"""To convert celsius into fahrenheit using lambda function"""
#def converter(x): return (x*9/5)+32
# C=[2,37,25,-1,0,100]
# #F=list(map(converter,C))
# #print(F)
# 
# F=list(map( lambda f: f*9/5+32 , C))
# print(F)

#3
# import math
# angle = (0, 30, 45, 60)
# function1 = map(lambda x: math.sin , angle )
# print(list(function1))
# 
# #4
# fib_series = []
# f0 = 0
# f1 = 1
# fib_series = []
# fib_series.append(f0)
# fib_series.append(f1)
# for i in range(2, 26):
#     f2 = f0 + f1
#     fib_series.append(f2)
#     f0 = f1
#     f1 = f2
# 
# odd_fibs = list(filter(lambda x: x % 2 != 0, fib_series))
# print(fib_series)
# print(odd_fibs)

#5
# from functools import reduce
# a = [3,7,4,8,3,]
# added = reduce(lambda x,y: x+y,a)
# print(added)

#6
# def cell_metabolism(glucose, oxygen):
# 
#     def energy_output(): 
#         return min(glucose,oxygen // 6) * 38
#     total_atp = energy_output()
#     return total_atp
# g = int(input( "g :"))
# o = int(input( "o :"))
# print(cell_metabolism(g,o))
    
#7
# def analyse_dna (sequence):
#     def gc_content():
#         TOTAL = sequence.count('G') + sequence.count('C')
#         return (TOTAL / len(sequence)) * 100
#     nonlocal gc = gc_content()
#     return gc
# if gc > 50:
#     print("gc rich")
# else:
#     print("at rich")
# dna = analyse_dna('GCTDHMFGJFGEIRHFEFJFEEHDOUHFLKCMDDJW')
# print(dna)   

#8
# def protien_energy(temp):
#     def calculate_free_energy(h,s,t):
#         g=h-(t*s)
#         return g
#     enthalpy=float(input("Enthalpy: "))
#     entropy=float(input("Entropy:"))
#     G=calculate_free_energy(enthalpy,entropy,temp)
#     if G<0:
#         return "stable"
#     else:
#         return "nonstable"
# 
# p1=protien_energy(25)
# print(p1)
 
#9
# import math
# 
# def population_growth(initial,rate,time):
#     def exponential_growth(i,r,t):
#         return i+math.e**(r*t)
#     nt=round(exponential_growth(initial,rate,time))
#     print(nt)
# 
# N=population_growth(10,2,10)
# print(N)

#10
# a=input("Enter a string: ")
# b=list(filter((lambda b: b in "aeiouAEIOU"), a.lower()))
# print("".join(b))

#11
# from functools import reduce
# 
# a=["A","p","p","l","e"," ",'i','s',' ','a',' ',"g","o","o","d"," ","f","r","u","i","t"]
# b=reduce((lambda a,b: a+b) , a)
# print(a)
# print(b)