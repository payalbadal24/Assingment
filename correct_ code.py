def prit(n, isPrime):
    isPrime[0] = isPrime[1] = False
    for i in range(2, n):
        isPrime[i] = True

    for p in range(2, n + 1):
        if p * p <= n and isPrime[p]:
            for i in range(p * 2, n + 1, p):
                isPrime[i] = False

def superPrimes(n):
    isPrime = [1 for i in range(n + 1)]
    prit(n, isPrime)
    primes = [0 for i in range(2, n + 1)]
    j = 0
    for p in range(2, n + 1):
        if isPrime[p]:
            primes[j] = p
            j += 1

    for k in range(j):
        if isPrime[primes[k]]:
            print(primes[k], end=" ")

n = 241
print("Super-Primes less than or equal to", n, "are:")
superPrimes(n)
