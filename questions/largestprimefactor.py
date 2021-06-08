# divide number by 2, 3, 5 and 7, until an integer is not returned
# find prime numbers of a number
# find the largest prime number


def largest_prime_number(num):
    prime_factor = 1
    int = 2
    while int <= num / int:


        if num % int == 0:
            print(f"int = {int}")
            print(f"num = {num}")
            prime_factor = int
            num /= int

        else:
            int += 1

    if prime_factor < num:
        prime_factor = num

    return prime_factor

print(largest_prime_number(600851475143))