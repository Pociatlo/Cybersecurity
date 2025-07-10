import random
from sympy import isprime

# === Algorytmy matematyczne ===
def gcd(a, b):
    """
    Oblicza największy wspólny dzielnik (NWD) liczb a i b metodą Euklidesa.
    """
    while b:
        a, b = b, a % b
    return a

def modinv(a, m):
    """
    Oblicza modularną odwrotność a modulo m, czyli liczbę x taką, że (a * x) % m == 1.
    Wykorzystuje rozszerzony algorytm Euklidesa.
    """
    m0 = m
    x0, x1 = 0, 1
    while a > 1:
        q = a // m
        a, m = m, a % m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

# === Generowanie liczb pierwszych ===
def generate_prime(bits=8):
    """
    Generuje losową liczbę pierwszą o zadanej liczbie bitów.
    Używa sympy.isprime do dokładnego testu pierwszości.
    """
    while True:
        p = random.getrandbits(bits)
        p |= 1  # upewnij się, że liczba jest nieparzysta (parzysta nie może być pierwsza oprócz 2)
        if isprime(p):
            return p

# === Generacja kluczy RSA ===
def generate_rsa_keys(bits=8):
    """
    Generuje parę kluczy RSA o kluczu n-bitowym.
    Zwraca krotkę (e, d, n) gdzie:
      - e to klucz publiczny (wykładnik),
      - d to klucz prywatny (odwrotność modularna e modulo φ(n)),
      - n to moduł RSA.
    
    Procedura:
    1. Generuje dwie różne liczby pierwsze p i q.
    2. Oblicza n = p * q oraz φ(n) = (p-1)*(q-1).
    3. Wybiera wykładnik e (domyślnie 65537, jeśli jest względnie pierwszy z φ(n), 
       w przeciwnym razie losuje e).
    4. Oblicza d jako modularną odwrotność e modulo φ(n).
    """
    print(f"🔧 Generuję liczby pierwsze {bits}-bitowe...")
    p = generate_prime(bits)
    q = generate_prime(bits)
    while p == q:
        q = generate_prime(bits)

    n = p * q
    phi = (p - 1) * (q - 1)

    print(f"✅ p = {p}")
    print(f"✅ q = {q}")
    print(f"✅ n = {n}")
    print(f"✅ φ(n) = {phi}")

    # === e – 65537 albo losowe względnie pierwsze z φ(n) ===
    e = 65537
    if gcd(e, phi) != 1:
        print("⚠️ 65537 się nie nadaje, wybieram losowe e...")
        e = random.randrange(3, phi, 2)
        while gcd(e, phi) != 1:
            e = random.randrange(3, phi, 2)

    d = modinv(e, phi)

    print(f"🔐 Public key:  (e = {e}, n = {n})")
    print(f"🔐 Private key: (d = {d}, n = {n})")

    return (e, d, n)


generate_rsa_keys()
