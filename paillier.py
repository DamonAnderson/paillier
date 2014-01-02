import rabinMiller, random, crypton

# Class implementing the Paillier cryptosystem
# Includes some homomorphic operations
class Paillier:

    # Initialize upon construction
    def __init__(self, keysize=1024):
        self.n,self.g,self.__lam,self.__mu = self.generateKey(keysize)

    # Generate a key (default size is 1024 bits)
    def generateKey(self, keysize=1024):
        p = rabinMiller.generateLargePrime(keysize)
        q = rabinMiller.generateLargePrime(keysize)
        n = p*q
        g = n + 1
        lam = (p-1)*(q-1)
        mu = crypton.mod_inv(lam, n)
        return n, g, lam, mu

    # Encrypt a plaintext message
    def encrypt(self, msg):
        r = random.randint(1, self.n-1)
        return (crypton.mod_pow(self.g, msg, self.n*self.n) * crypton.mod_pow(r, self.n, self.n*self.n)) % (self.n*self.n)

    # Decrypt a ciphertext
    def decrypt(self, c):
        u = crypton.mod_pow(c, self.__lam, self.n*self.n)
        return (((u-1) // self.n) * self.__mu) % self.n

    # Add a plaintext integer (a) to the ciphertext (c)
    def add_plain(self, c, a):
        return (c * crypton.mod_pow(self.g,a,self.n*self.n)) % (self.n*self.n)

    # Add one ciphertext (a) to another ciphertext (c)
    def add_cipher(self, c, a):
        return (c * a) % (self.n*self.n)

    # Subtract a plaintext integer (a) from the ciphertext (c)
    def sub_plain(self, c, a):
        gi = crypton.mod_inv(self.g, self.n*self.n)
        return (c * crypton.mod_pow(gi,a,self.n*self.n)) % (self.n*self.n)

    # Subtract one ciphertext (a) from another ciphertext (c)
    def sub_cipher(self, c, a):
        gi = crypton.mod_inv(self.g, self.n*self.n)
        return (c * crypton.mod_pow(gi,a,self.n*self.n)) % (self.n*self.n)

    # Multiply the ciphertext (c) by a plaintext integer (a)
    def mul_plain(self, c, a):
        return crypton.mod_pow(c,a,self.n*self.n)
