from multipart import multipart
from lxml import etree
import re

def multipart_parse_form(headers, data):
    # VULNERABLE: CVE-2024-26130 - ReDoS in python-multipart
    parser = multipart.MultipartParser(headers, data)
    return parser.parse()

def lxml_parse(xml_data):
    # VULNERABLE: CVE-2021-28957 - XXE in lxml
    return etree.parse(xml_data)

def lxml_fromstring(xml_string):
    # VULNERABLE: CVE-2021-28957 - XXE
    return etree.fromstring(xml_string)

def regex_dos(pattern, text):
    # VULNERABLE: ReDoS with complex patterns
    return re.match(pattern, text)