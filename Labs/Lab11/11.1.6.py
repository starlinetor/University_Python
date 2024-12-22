from math import floor, sqrt

def sieve_of_eratosthenes(n : int) -> list[int]:
    prime_numbers : list[int] = [i for i in range(2,n+1)]
    max_prime : int = floor(sqrt(n))
    for i in range(2,max_prime):
        if i not in prime_numbers:
            continue    
        for j in range(2,floor(n/i)+1):
            if i*j in prime_numbers:
                prime_numbers.remove(i*j)
    return prime_numbers

print(sieve_of_eratosthenes(100000))