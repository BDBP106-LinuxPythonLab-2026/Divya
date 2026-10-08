#1
a = [i for i in range(50)]
#print(a)
# print(a[1:5])
# print(a[3:20:2])
#print(a[::2])
# print(a[::])
# print(a[10::2])
# print(a[1:1:1])
# print(a[-7::1])
#print(a[-6:])
#print(a[-10:-4])

#print(a[::-1])
#print(a[::-3])
#print(a[:1:-2])
# (d) a[-1:-1:-1]
# (e) a[:-5:-1]
# (f) a[:0:-1]
# (g) a[:-1:-1]
# (h) a[0:-5:-1]
# (i) a[-1:5:-1]
# (j) a[2:2:-1]
# (k) a[2:1:-1]
#print(a[0:-5])

#1)2)  print(a[2::2])

#1)3)  new_list = a[:10] + list(range(36, 51, 2))
#print(new_list)

#2)1  
# total = sum([i for i in a])
# print(total)

# 2)2
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
# b = [i for i in range(50) if is_prime(i)]
# print(b)

#2)3
# c=[j for i in a for j in b if j==i]
# print("c :"+str(c))


#3)1)1
# result = ",".join([str(i) for i in a])
# print(result)

#3)1)2
# result = ".".join(str(i) for i in a)
# print(result)

#3)1)3
# result = "_".join(str(i) for i in a)
# print(result)

#3)1)4
#sq=[i*i for i in a]
# d="\n".join([" ".join([str(a[i]),str(sq[i])]) for i in range(0,len(a))])
# print(d)

#3)2)1
# n=["mahima shukla","manekha verma",'tanishq kokate',"mahaprasad nayak","kaumudi priyadarshani","sneha bhattacharya","shravan pawale","sanjana pillai","ishika pandey","aashi dubey"]
# uc=[i.upper() for i in n]
# print(uc)

#3)2)2
# swp=[" ".join([name.split()[1],name.split()[0]]) for name in n]
# print(swp)

#3)2)3
# fl=[".".join([(p.title()).split()[0],(p.title()).split()[1]]) for p in n]
# print(fl)

#3)3)1
# s="she sells sea shells that she collects from the sea floor"
# longestword=[max([word for word in s.split()], key=len)]
# print("The longest word is :"+str(longestword))

#3)3)2
# rw=[s.split()[i] for i in range(0,len(s.split())) for j in range((i+1),len(s.split())) if s.split()[i]==s.split()[j]]
# print("The repeated words are: "+str(rw))