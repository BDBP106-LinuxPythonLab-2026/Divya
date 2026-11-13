import numpy as np

# 1
# arr_i = np.arange(10)
# print(arr_i)

# 2
# arr_ii = np.ones((3, 3), dtype=bool)
# print(arr_ii)

# 3
# def is_prime(n):
#     if n < 2: return False
#     return all(n % i != 0 for i in range(2, int(n**0.5) + 1))
# 
# arr_iii_base = np.arange(1, 51)
# arr_iii = arr_iii_base[np.array([is_prime(x) for x in arr_iii_base])]
# 
# print("Base Array:\n", arr_iii_base)
# print("Filtered Prime Array:\n", arr_iii)


# 4
# rg = np.random.default_rng(1) 
# arr_iv_2d = arr_iv_1d.reshape(4, 5)
# 
# print("1D Random Array:\n", arr_iv_1d)
# print("Reshaped 4x5 Array:\n", arr_iv_2d)


# 5
# a_v = np.arange(10)
# b_v = np.ones(10, dtype=int)
# stacked_v = np.hstack((a_v, b_v))
# 
# print("Array a:", a_v)
# print("Array b:", b_v)
# print("Stacked Horizontally:", stacked_v)

# Helper to generate the first 100 primes
primes_list = []
candidate = 2
while len(primes_list) < 100:
    if is_prime(candidate): primes_list.append(candidate)
    candidate += 1

a_vi = np.arange(1, 101)
b_vi = np.array(primes_list)
intersection_vi = np.intersect1d(a_vi, b_vi)

print("Array a (1-100):\n", a_vi)
print("Array b (First 100 primes):\n", b_vi)
print("Intersection:\n", intersection_vi)


