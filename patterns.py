"""Wrappers that call specific library functions requested for SCA testing.
Each function is intentionally simple and calls the named library API.
DO NOT use in production with untrusted inputs.
"""

import zipfile

try:
    import torch
except Exception:
    torch = None

try:
    from werkzeug.utils import safe_join
except Exception:
    safe_join = None

try:
    import feedparser
except Exception:
    feedparser = None

try:
    from cryptography.hazmat.primitives import hashes
except Exception:
    hashes = None

try:
    import nltk
except Exception:
    nltk = None

try:
    import paramiko
except Exception:
    paramiko = None

try:
    import libarchive
except Exception:
    libarchive = None


def torch_load_weights(path):
    """Call torch.load with weights_only=True (per user request)."""
    if torch is None:
        raise RuntimeError('torch not installed')
    return torch.load(path, weights_only=True)


def werkzeug_safe_join_wrapper(base, *paths):
    if safe_join is None:
        raise RuntimeError('werkzeug not installed')
    return safe_join(base, *paths)


def feedparser_parse_wrapper(data):
    if feedparser is None:
        raise RuntimeError('feedparser not installed')
    return feedparser.parse(data)


def cryptography_stub_usage():
    if hashes is None:
        raise RuntimeError('cryptography not installed')
    d = hashes.Hash(hashes.SHA256())
    d.update(b'example')
    return d.finalize()


def nltk_trigger_download(resource='punkt'):
    if nltk is None:
        raise RuntimeError('nltk not installed')
    return nltk.download(resource)


def paramiko_transport_auth_stub():
    if paramiko is None:
        raise RuntimeError('paramiko not installed')
    return {'Transport': getattr(paramiko, 'Transport', None)}


def zipfile_extract_wrapper(zip_path, member=None, extract_dir='.'):
    with zipfile.ZipFile(zip_path, 'r') as z:
        if member is None:
            z.extractall(path=extract_dir)
            return 'extracted_all'
        else:
            z.extract(member, path=extract_dir)
            return f'extracted:{member}'
