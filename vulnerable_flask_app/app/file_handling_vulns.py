import zipfile
import tarfile
import os

def zip_extract_all(zip_path, extract_path):
    # VULNERABLE: CVE-2018-1000802 - Path traversal in zipfile
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)

def zip_extract(zip_path, extract_path, member):
    # VULNERABLE: CVE-2018-1000802 - Path traversal
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extract(member, extract_path)

def tar_extract_all(tar_path, extract_path):
    # VULNERABLE: CVE-2007-4559 - Path traversal in tarfile
    with tarfile.open(tar_path, 'r') as tar_ref:
        tar_ref.extractall(extract_path)