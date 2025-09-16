#!/usr/bin/env python3
# Simple Python app demonstrating vulnerable method usage for Veracode SCA testing.
# This calls rsa.verify(), which is vulnerable to BERserk (CVE-2016-1494) in rsa<3.3.

import rsa  # Vulnerable library import
import urllib3  # Another vulnerable dep (for dependency vuln detection)

def perform_verification():
    """
    Function that calls the vulnerable rsa.verify() method.
    In a real app, this might verify signatures; here it's dummy data to make the call reachable.
    Veracode SCA will detect this as a reachable vulnerable method via call graph analysis.
    """
    # Dummy public key (N=modulus, E=exponent) - in practice, load from PEM
    pubkey = rsa.PublicKey(12345, 65537)  # Minimal dummy key for demo
    
    # Dummy hash and signature (bytes) - triggers the vulnerable verify logic
    message_hash = b"Sample message hash for verification"
    signature = b"Dummy signature bytes that could be malformed for BERserk attack"
    
    try:
        # VULNERABLE METHOD CALL: rsa.verify() is exploitable in rsa==3.0
        # BERserk allows signature spoofing with small exponents and malformed ASN.1 DER.
        is_valid = rsa.verify(message_hash, signature, pubkey)
        print(f"Verification result: {is_valid}")
    except rsa.VerificationError:
        print("Verification failed (expected for dummy data)")
    except Exception as e:
        print(f"Error during verification: {e}")

def fetch_data():
    """
    Example usage of urllib3 (vulnerable dep) to trigger dependency detection.
    No specific vulnerable method here, but the lib version has CVEs.
    """
    http = urllib3.PoolManager()
    try:
        response = http.request('GET', 'https://httpbin.org/get')
        print(f"Fetched data status: {response.status}")
    except Exception as e:
        print(f"Fetch error: {e}")

if __name__ == "__main__":
    print("Running vulnerable Python app for Veracode SCA testing...")
    perform_verification()  # Ensures vulnerable method is reachable
    fetch_data()  # Ensures urllib3 dep is used
    print("App execution complete.")