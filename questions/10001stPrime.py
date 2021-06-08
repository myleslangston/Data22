# prime_num = 1
# n = 1
# int = 1
#
# while n <= 10001:
#     if prime_num % int == 0:
#         prime_num += 1
#         int += 1
#     else:
#         int += 1


def isPrime(n):
    if n < 2: return "Neither prime, nor composite"
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# returns the nth prime number
def nthPrime(n):
    numberOfPrimes = 0
    prime = 1

    while numberOfPrimes < n:
        prime += 1
        if isPrime(prime):
            numberOfPrimes += 1
    return prime

print(nthPrime(10001))