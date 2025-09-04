import requests
import urllib3
from urllib.request import urlopen

def requests_get(url, **kwargs):
    # VULNERABLE: CVE-2023-32681 - SSRF and credential leaks
    return requests.get(url, **kwargs)

def requests_post(url, **kwargs):
    # VULNERABLE: CVE-2023-32681
    return requests.post(url, **kwargs)

def session_request(session, method, url, **kwargs):
    # VULNERABLE: CVE-2023-32681
    return session.request(method, url, **kwargs)

def urllib3_request(url, **kwargs):
    # VULNERABLE: CVE-2023-45803 - SSRF and redirect issues
    http = urllib3.PoolManager()
    return http.request('GET', url, **kwargs)

def urllib_urlopen(url):
    # VULNERABLE: SSRF potential
    return urlopen(url)