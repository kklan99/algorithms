def prime_sum(n):
    """
    Given a number n, returns two prime numbers that add up to n
    """
    primes = get_prime_numbers(n)

    for i in range(len(primes)):

        if primes[i] and primes[n-i]:
            return [i, n-i]
        

def get_prime_numbers(n):
    """
    Given an upper bound, returns a list of prime numbers from 0 to n inclusive,
    with True designating a prime number. Based on Sieve of Erathosthenes 
    algorithm.
    """
    # Initialize all numbers to be prime
    primes = [True] * (n+1)

    # Start with first prime number to be 2.
    i = 2

    while i * i <= n:

        # If prime[i] is still true, then it is prime. Now, we find all 
        # multiples of i and set them to be false.
        if primes[i]:

            # All multiples of i are not prime.
            for j in range(i*2, n+1, i):

                primes[j] = False

        i += 1

    return primes

def main():
    print(prime_sum(4))
    print(prime_sum(200))

if __name__ == '__main__':
    main()
