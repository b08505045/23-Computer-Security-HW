from Crypto.Util.number import getPrime, isPrime, GCD, bytes_to_long, long_to_bytes
from random import randrange
from hashlib import sha256
from sympy.ntheory.modular import solve_congruence

def xorrrrr(nums):
    n = len(nums)
    result = [0] * n
    for i in range(1, n):
        result = [ result[j] ^ nums[(j+i) % n] for j in range(n)]
    return result

def modular_inverse(a, m):
    x, y, g = extend_gcd(a, m)
    if g != 1:
        raise Exception("The modular inverse does not exist")
    else:
        return x % m

def extend_gcd(a, b):
    if b == 0:
        return (1, 0, a)
    else:
        (a1, b1, g) = extend_gcd(b, a % b)
        return (b1, a1 - (a // b) * b1, g)
    
def xgcd(a, b):
        """return (x, y) such that a*x + b*y = gcd(a, b)"""
        x0, x1, y0, y1 = 0, 1, 1, 0
        while a != 0:
            (q, a), b = divmod(b, a), a
            y0, y1 = y1, y0 - q * y1
            x0, x1 = x1, x0 - q * x1
        return x0, y0

# xored 
xor_hint = [297901710, 2438499757, 172983774, 2611781033, 2766983357, 1018346993, 810270522, 2334480195, 154508735, 1066271428, 3716430041, 875123909, 2664535551, 2193044963, 2538833821, 2856583708, 3081106896, 2195167145, 2811407927, 3794168460]
xor_muls = [865741, 631045, 970663, 575787, 597689, 791331, 594479, 857481, 797931, 1006437, 661791, 681453, 963397, 667371, 705405, 684177, 736827, 757871, 698753, 841555]
xor_mods = [2529754263, 4081964537, 2817833411, 3840103391, 3698869687, 3524873305, 2420253753, 2950766353, 3160043859, 2341042647, 4125137273, 3875984107, 4079282409, 2753416889, 2778711505, 3667413387, 4187196169, 3489959487, 2756285845, 3925748705]

# reconstrcut hint, muls & mods
hint = xorrrrr(xor_hint)
muls = xorrrrr(xor_muls)
mods = xorrrrr(xor_mods)

# construct mul_inverse
mul_inverse = list(map(modular_inverse, muls, mods))

# secret = hint[i] * mul_invese[i] % mod[i]
secret = [(hint[i] * mul_inverse[i]) % mods[i] for i in range(len(hint))]

# CRT
# x ≡ ai (mod ni)
# a = secret[i], n_i = mod[i], N = pi(mod[i]), bi = N/n_i
congruences = []
for i in range(len(secret)):
    congruences.append((secret[i], mods[i]))

x = solve_congruence(*congruences)

x_value, N = x
print(long_to_bytes(x_value))