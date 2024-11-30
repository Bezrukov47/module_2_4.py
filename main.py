numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
def is_prime(j):
    if j<= 1:
        return False
    for i in range(2, int(j**0.5) + 1):
        if j % i == 0:
            return False
    return True
primes = [num for num in numbers if is_prime(num)]
print(primes)
primes = [2, 3, 5, 7, 11, 13]
not_primes = [num for num in numbers if not is_prime(num)]
# print (not_primes)
print("Простые числа:", primes)
print("Непростые числа:", not_primes)