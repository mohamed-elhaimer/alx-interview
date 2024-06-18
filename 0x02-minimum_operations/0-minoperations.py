#!/usr/bin/python3
"""find minimum operation to reach a exact number of H"""


def isprime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def nmbr_premier(n: int) -> list:
    premier = []
    for i in range(2, n + 1):
        if isprime(i):
            premier.append(i)
    return premier


def minOperations(n: int) -> int:
    if n <= 1:
        return 0

    result = []
    primes = nmbr_premier(n)

    while n > 1:
        for prime in primes:
            while n % prime == 0:
                result.append(prime)
                n /= prime

    return sum(result)
