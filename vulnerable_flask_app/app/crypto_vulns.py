import rsa
from cryptography.hazmat.primitives.asymmetric import rsa as crypto_rsa
from cryptography.hazmat.backends import default_backend

def rsa_decrypt(ciphertext, priv_key):
    # VULNERABLE: CVE-2020-13757 - BERserk attack in rsa library
    return rsa.decrypt(ciphertext, priv_key)

def rsa_verify(message, signature, pub_key):
    # VULNERABLE: CVE-2020-13757
    return rsa.verify(message, signature, pub_key)

def generate_weak_rsa_key(key_size=512):
    # VULNERABLE: CVE-2020-36242 - Weak RNG in cryptography
    return crypto_rsa.generate_private_key(
        public_exponent=65537,
        key_size=key_size,
        backend=default_backend()
    )