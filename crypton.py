# Crypton library
# Just a few handy functions for doing cryptography

# Greatest Common Divisor - uses the Euclidean algorithm
def gcd(a,b):
    while a != 0:
        a,b = b%a,a
    return b

# Modular inverse - uses the Extended Euclidean algorithm
def mod_inv(a,m):
    if gcd(a,m) != 1:
        return None
    u1,u2,u3 = 1,0,a
    v1,v2,v3 = 0,1,m
    while v3 != 0:
        q = u3 // v3
        v1,v2,v3,u1,u2,u3 = (u1-q*v1),(u2-q*v2),(u3-q*v3),v1,v2,v3
    return u1 % m

# Modular Exponentiation - implements binary exponentiation
def mod_pow(a,b,m):
    result = 1
    while b > 0:
        if b % 2 == 1:
            result = (result*a) % m
        b = b>>1
        a = (a*a) % m
    return result
