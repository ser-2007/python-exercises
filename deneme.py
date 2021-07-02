
# Python program to illustrate...
# To print total number of twin prime
# using Sieve of Eratosthenes
 
def printTwinPrime(n):
     
    # Create a boolean array "prime[0..n]"
    # and initialize all entries it as
    # true. A value in prime[i] will
    # finally be false if i is Not a prime,
    # else true.
    prime = [True for i in range(n + 2)]
    p = 2
     
    while (p * p <= n + 1):
         
        # If prime[p] is not changed,
        # then it is a prime
        if (prime[p] == True):
             
            # Update all multiples of p
            for i in range(p * 2, n + 2, p):
                prime[i] = False
        p += 1
     
    # check twin prime numbers
    # display the twin prime numbers
    for p in range(2, n-1):
        if prime[p] and prime[p + 2]:
            print("(",p,",", (p + 2), ")" ,end='')
 
 printTwinPrime(8)