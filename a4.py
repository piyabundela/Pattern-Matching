import random
import math


# return appropriate N that satisfies the error bounds
def findN(eps, m):
    return (m * math.log(26, 2) / eps) ** 2


def change(x):
    if x == '?':
        return 0
    return ord(x) - 65


# Return sorted list of starting indices where p matches x
def modPatternMatch(q, pat, txt):
    d = 26  # d is the number of characters in the input alphabet
    m = len(pat)
    n = len(txt)
    p = 0  # hash value for pattern
    t = 0  # hash value for text
    match = []

    h = 1
    for i in range(m - 1):
        h = (h * d) % q
        print(h)
    if m > n:
        return match

    for i in range(m):
        p = (d * p + change(pat[i])) % q
        t = (d * t + change(txt[i])) % q

    for i in range(n - m + 1):
        if p == t:
            match.append(i)
        if i != n - m:
            t = ((t - (h * change(txt[i])) % q) * 26 + change(txt[i + m])) % q
        continue

    return match


# Return sorted list of starting indices where p matches x
def modPatternMatchWildcard(q, pat, txt):
    d = 26  # d is the number of characters in the input alphabet
    m = len(pat)
    n = len(txt)
    p = 0  # hash value for pattern
    t = 0  # hash value for text
    match = []

    if m > n:
        return match

    h = 1
    for i in range(m - 1):
        h = (h * d) % q

    ind = pat.index('?')
    index_ = 1
    for i in range(m - ind - 1):
        index_ = (index_ * d) % q

    for i in range(m):
        p = (d * p + change(pat[i])) % q
        t = (d * t + change(txt[i])) % q

    for i in range(n - m + 1):
        r = (t - (index_ * change(txt[i + ind])) % q) % q
        if p == r:
            match.append(i)
        if i != n - m:
            t = ((t - (h * change(txt[i])) % q) * 26 + change(txt[i + m])) % q
        continue

    return match


# To check if a number is prime
def isPrime(q):
    if q > 1:
        for i in range(2, int(math.sqrt(q)) + 1):
            if q % i == 0:
                return False
        return True
    else:
        return False


# To generate random prime less than N
def randPrime(N):
    primes = []
    for q in range(2, N + 1):
        if isPrime(q):
            primes.append(q)
    return primes[random.randint(0, len(primes) - 1)]


# pattern matching
def randPatternMatch(eps, p, x):
    N = findN(eps, len(p))
    q = randPrime(N)
    return modPatternMatch(q, p, x)


# pattern matching with wildcard
def randPatternMatchWildcard(eps, p, x):
    N = findN(eps, len(p))
    q = randPrime(N)
    return modPatternMatchWildcard(q, p, x)


