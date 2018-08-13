def genPrimes():
    primes = [2]
    number = 2
    while True:
        for prime in primes:
            if number % prime != 0:
                ifprime = True
            else:
                ifprime = False
        if ifprime == True:
            primes.append(prime)
            yield prime
        number += 1
