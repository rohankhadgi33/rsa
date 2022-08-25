import stdio
import stdrandom
import sys


# Generates and returns the public/private keys as a tuple (n, e, d). Prime numbers p and q
# needed to generate the keys are picked from the interval [lo, hi).
def keygen(lo, hi):
    # get list of primes from the interval [lo, hi)
    a = _primes(lo, hi)
    k = len(a)

    # make a shuffled list from a up to k elements
    samples = _sample(a, k)
    # get p and q from samples which are distinct
    p = samples[stdrandom.uniformInt(0, k)]
    q = samples[stdrandom.uniformInt(0, k)]
    while q == p:
        q = samples[stdrandom.uniformInt(0, k)]
    n = p * q  # get n
    m = (p - 1) * (q - 1)  # get m

    # get new list of primes
    new_primes = _primes(2, m)
    # choose e from new list that does not divide m
    e = new_primes[stdrandom.uniformInt(0, len(new_primes))]
    while m % e == 0:
        e = new_primes[stdrandom.uniformInt(0, len(new_primes))]
    # choose d randomly from [1,m) which satisfies equation
    d = stdrandom.uniformInt(1, m)
    while (e * d) % m != 1:
        d = stdrandom.uniformInt(1, m)
    return n, e, d  # return tuple


# Encrypts x (int) using the public key (n, e) and returns the encrypted value.
def encrypt(x, n, e):
    return (x ** e) % n


# Decrypts y (int) using the private key (n, d) and returns the decrypted value.
def decrypt(y, n, d):
    return (y ** d) % n


# Returns the least number of bits needed to represent n.
def bitLength(n):
    return len(bin(n)) - 2


# Returns the binary representation of n expressed in decimal, having the given width, and padded
# with leading zeros.
def dec2bin(n, width):
    return format(n, '0%db' % (width))


# Returns the decimal representation of n expressed in binary.
def bin2dec(n):
    return int(n, 2)


# Returns a list of primes from the interval [lo, hi).
def _primes(lo, hi):
    primes = []  # create empty list
    # in a loop compute for prime numbers and put them in a list
    for i in range(lo, hi):
        j = 2
        while j <= i / j:
            if i % j == 0:
                break
            j += 1
        if j > i / j and i >= 2:
            primes += [i]
    return primes


# Returns a list containing a random sample (without replacement) of k items from the list a.
def _sample(a, k):
    sample = a[0:k]  # make a list sample copy of a
    # in loop compute to get a shuffled list up to k elements
    for i in range(k):
        r_index = stdrandom.uniformInt(0, k)  # get random value
        # shuffle the list
        temp = sample[r_index]
        sample[r_index] = sample[i]
        sample[i] = temp
    return sample  # return shuffled list


# Returns a random item from the list a.
def _choice(a):
    r = stdrandom.uniformInt(0, len(a))  # random value
    return a[r]  # return  r element of a


# Unit tests the library [DO NOT EDIT].
def _main():
    x = ord(sys.argv[1])
    n, e, d = keygen(25, 100)
    encrypted = encrypt(x, n, e)
    stdio.writef('encrypt(%c) = %d\n', x, encrypted)
    decrypted = decrypt(encrypted, n, d)
    stdio.writef('decrypt(%d) = %c\n', encrypted, decrypted)
    width = bitLength(x)
    stdio.writef('bitLength(%d) = %d\n', x, width)
    xBinary = dec2bin(x, width)
    stdio.writef('dec2bin(%d) = %s\n', x, xBinary)
    stdio.writef('bin2dec(%s) = %d\n', xBinary, bin2dec(xBinary))


if __name__ == '__main__':
    _main()