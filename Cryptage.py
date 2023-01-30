def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x

def InverseModulaire(e, Phi_n):
    gcd, x, y = extended_gcd(e, Phi_n)
    return x

def findPrimeToPhiN(PhiN):
    e = 0
    for k in range(2, PhiN):
        gcd, u, v = extended_gcd(k, PhiN)
        if gcd == 1:
            e = k
            print(e)
            break

def generatePublicKey(p, q):
    phiN = (q-1)*(p-1)
    
    return p*q, findPrimeToPhiN(phiN)

def generatePrivateKey(p, q):
    phiN = (q-1)*(p-1)
    return InverseModulaire(findPrimeToPhiN(phiN), phiN), p*q

def encrypt(message, n, e):
    return pow(message, e, n)

def decrypt(message, d, n):
    return pow(message, d, n)