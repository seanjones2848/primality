# testing for bases using miller-rabin test
# testing odd numbers only
# using set bases for numbers of different sizes
# find a rpime using random number generation
# when found, print to file if not already in file
import random
import time

# find a single prime within a 1000 random numbers
def find_prime():
    # failsafe to make sure it isn't checking more than a thousand random numbers at a time to find a prime
    fail_safe = 1000
    while fail_safe > 0:
        fail_safe -= 1
        # randrange used to only grab odd numbers in range
        n = random.randrange(3, 1122004669633, 2)
        if miller_rabin(n):
            print_prime(n)
            return n
    return 0

# run and keep finding new primes until I end the program
# display how long it takes to generate 1000 new primes
def find_prime_loop():
    prime_count = 0
    start_time = time.perf_counter()
    while 1:
        n = random.randrange(3, 1122004669633, 2)
        if miller_rabin(n):
            print_prime(n)
            prime_count += 1
        if prime_count % 1000 == 0:
            end_time = time.perf_counter()
            print(end_time - start_time)
            start_time = time.perf_counter()


# test to see if n is prime
# only need to run on small set of bases for "small" primes
def miller_rabin(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    if n <= 2047:
        return miller_rabin_inner(2, n)
    if n <= 1373653:
        return (miller_rabin_inner(2, n) & miller_rabin_inner(3, n))
    if n <= 9080191:
        return (miller_rabin_inner(31, n) & miller_rabin_inner(73, n))
    if n <= 25326001:
        return (miller_rabin_inner(2, n) & miller_rabin_inner(3, n) & miller_rabin_inner(5, n))
    if n <= 3215031751:
        return (miller_rabin_inner(2, n) & miller_rabin_inner(3, n) & miller_rabin_inner(5, n) & miller_rabin_inner(7, n))
    if n <= 4759123141:
        return (miller_rabin_inner(2, n) & miller_rabin_inner(7, n) & miller_rabin_inner(61, n))
    if n <= 1122004669633:
        return (miller_rabin_inner(2, n) & miller_rabin_inner(13, n) & miller_rabin_inner(23, n) & miller_rabin_inner(1662803, n))

# run miller_rabin on n for base a
def miller_rabin_inner(a, n):
    d = n - 1
    while d % 2 == 0:
        d //= 2
    x = pow(a, d, n)
    if x == 1 or x == n - 1:
        return True
    while d != n - 1:
        x = (x * x) % n
        d *= 2
        if x == 1:
            return False
        if x == n - 1:
            return True
    return False

def print_prime(n):
    #print(n)
    f = open("primes.txt", "r")
    primes = set([int(x.strip()) for x in list(f)])
    if n not in primes:
        f = open("primes.txt", "a")
        f.write(f'{n}\n')

find_prime_loop()
