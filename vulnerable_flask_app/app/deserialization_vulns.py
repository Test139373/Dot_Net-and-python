import yaml
import pickle
import marshal

def yaml_deserialize(data):
    # VULNERABLE: CVE-2017-18342, CVE-2020-1747 - PyYAML unsafe deserialization
    # Can execute arbitrary Python code
    return yaml.load(data, Loader=yaml.Loader)

def yaml_full_load(data):
    # VULNERABLE: CVE-2020-1747 - PyYAML unsafe deserialization
    return yaml.full_load(data)

def pickle_deserialize(data):
    # VULNERABLE: Arbitrary code execution via pickle
    return pickle.loads(data)

def marshal_deserialize(data):
    # VULNERABLE: Similar to pickle vulnerabilities
    return marshal.loads(data)