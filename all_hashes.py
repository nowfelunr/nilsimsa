from Crypto.Hash import MD2
import hashlib
import requests
import zlib
from fnvhash import fnv1a_32, fnv1_64, fnv1a_64
import mmh3
from pearhash import PearsonHasher
from ripemd128 import ripemd128



hash_api_base_url = "https://md5calc.com/hash"

listed_hasehs = [
    'md2', 'md5', 'md4', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512', 'ripemd128', 'ripemd160', 'ripemd256', 
    'ripemd320', 'whirlpool', 'snefru', 'snefru256', 'gost', 'adler32', 'crc32', 'fnv132', 'fnv164', 'fnv1a_64', 
    'fnv1a_32', 'joaat', 'mmh3', 'dbj2', 'sdbm', 'pearson', 'haval128_3', 'haval160_3', 'haval192_3', 'haval224_3', 
    'haval256_3', 'haval128_4', 'haval160_4', 'haval192_4', 'haval224_4', 'haval256_4', 'haval128_5', 'haval160_5', 
    'haval192_5', 'haval224_5','haval256_5'
    ]

def get_hash(text, hash_name):
    if hash_name not in listed_hasehs:
        raise Exception(f'{hash_name} is not supported')
    # print(f'get_{hash_name}' + f'("{text}")')
    result = eval(f'_get_{hash_name}' + f'("{text}")')
    return result


def convert_spaced_str(txt):
    data = ""
    for x in txt:
        if x != " ":
            data += x
        else: 
            data += "+"

    return data

def _get_md2(txt):
    md2 = MD2.new()
    md2.update(txt.encode('utf-8'))

    return md2.hexdigest()


def _get_md5(txt):
    return hashlib.md5(txt.encode('utf-8')).hexdigest()


def _get_md4(txt):
    h = hashlib.new('md4', txt.encode('utf-8'))
    return h.hexdigest()

def _get_sha1(txt):
    return hashlib.sha1(txt.encode('utf-8')).hexdigest()

def _get_sha224(txt):
    return hashlib.sha224(txt.encode('utf-8')).hexdigest()

def _get_sha256(txt):
    return hashlib.sha256(txt.encode('utf-8')).hexdigest()

def _get_sha384(txt):
    return hashlib.sha384(txt.encode('utf-8')).hexdigest()


def _get_sha512(txt):
    return hashlib.sha512(txt.encode('utf-8')).hexdigest()


def _get_ripemd128(txt):
    # h = hashlib.new('ripemd128', txt.encode('utf-8'))
    digest = ripemd128(txt.encode('utf-8'))
    return digest

def _get_ripemd160(txt):
    data = convert_spaced_str(txt)
    req = requests.get(f'{hash_api_base_url}/ripemd160.json/' + data)
    return req.text.replace('"', '')

def _get_ripemd256(txt):
    data = convert_spaced_str(txt)
    req = requests.get(f'{hash_api_base_url}/ripemd256.json/' + data)
    return req.text.replace('"', '')

def _get_ripemd320(txt):
   data = convert_spaced_str(txt)
   req = requests.get(f'{hash_api_base_url}/ripemd320.json/' + data)
   return req.text.replace('"', '')

def _get_whirlpool(txt):
    h = hashlib.new('whirlpool', txt.encode('utf-8'))
    return h.hexdigest()

def _get_snefru(txt):
    data = convert_spaced_str(txt)
    req = requests.get(f'{hash_api_base_url}/snefru.json/' + data)
    return req.text.replace('"', '')

def _get_snefru256(txt):
    data = convert_spaced_str(txt)
    req = requests.get(f'{hash_api_base_url}/snefru256.json/' + data)
    return req.text.replace('"', '')

def _get_gost(txt):
    data = convert_spaced_str(txt)
    req = requests.get(f'{hash_api_base_url}/gost.json/' + data)
    return req.text.replace('"', '')

def _get_adler32(txt):
    return zlib.adler32(txt.encode('utf-8'))

def _get_crc32(txt):
    return hex(zlib.crc32(txt.encode('utf-8'))% 2**32)

def _get_fnv132(txt):
    return hex(fnv1a_32(txt.encode('utf-8')))

def _get_fnv164(txt):
    return hex(fnv1_64(txt.encode('utf-8')))

def _get_fnv1a_64(txt):
    return hex(fnv1a_64(txt.encode('utf-8')))

def _get_fnv1a_32(txt):
    return hex(fnv1a_32(txt.encode('utf-8')))


def _get_joaat(txt):
    data = convert_spaced_str(txt)
    req = requests.get(f'{hash_api_base_url}/joaat.json/' + data)
    return req.text.replace('"', '')

def _get_mmh3(txt):
    return mmh3.hash(txt.encode('utf-8')) 

def _get_dbj2(txt):
    hash = 5381
    for x in txt:
        hash = (( hash << 5) + hash) + ord(x)
    return hash & 0xFFFFFFFF

def _get_sdbm(txt):
    hash_value = 0
    for plain_chr in txt:
        hash_value = (
            ord(plain_chr) + (hash_value << 6) + (hash_value << 16) - hash_value
        )
    return hash_value

def _get_pearson(txt):
    hasher = PearsonHasher(2)
    return hasher.hash(txt.encode('utf-8')).hexdigest()

def _get_haval128_3(txt):
    data = convert_spaced_str(txt)
    req = requests.get(f'{hash_api_base_url}/haval128-3.json/' + data)
    return req.text.replace('"', '')

def _get_haval160_3(txt):
    data = convert_spaced_str(txt)
    req = requests.get(f'{hash_api_base_url}/haval160-3.json/' + data)
    return req.text.replace('"', '')

def _get_haval192_3(txt):
    data = convert_spaced_str(txt)
    req = requests.get(f'{hash_api_base_url}/haval192-3.json/' + data)
    return req.text.replace('"', '')

def _get_haval224_3(txt):
    data = convert_spaced_str(txt)
    req = requests.get(f'{hash_api_base_url}/haval224-3.json/' + data)
    return req.text.replace('"', '')

def _get_haval256_3(txt):
    data = convert_spaced_str(txt)
    req = requests.get(f'{hash_api_base_url}/haval192-3.json/' + data)
    return req.text.replace('"', '')

def _get_haval128_4(txt):
    data = convert_spaced_str(txt)
    req = requests.get(f'{hash_api_base_url}/haval128-4.json/' + data)
    return req.text.replace('"', '')

def _get_haval160_4(txt):
    data = convert_spaced_str(txt)
    req = requests.get(f'{hash_api_base_url}/haval160-4.json/' + data)
    return req.text.replace('"', '')

def _get_haval192_4(txt):
    data = convert_spaced_str(txt)
    req = requests.get(f'{hash_api_base_url}/haval192-4.json/' + data)
    return req.text.replace('"', '')

def _get_haval224_4(txt):
    data = convert_spaced_str(txt)
    req = requests.get(f'{hash_api_base_url}/haval224-4.json/' + data)
    return req.text.replace('"', '')

def _get_haval256_4(txt):
    data = convert_spaced_str(txt)
    req = requests.get(f'{hash_api_base_url}/haval256-4.json/' + data)
    return req.text.replace('"', '')

def _get_haval128_5(txt):
    data = convert_spaced_str(txt)
    req = requests.get(f'{hash_api_base_url}/haval128-5.json/' + data)
    return req.text.replace('"', '')

def _get_haval160_5(txt):
    data = convert_spaced_str(txt)
    req = requests.get(f'{hash_api_base_url}/haval160-5.json/' + data)
    return req.text.replace('"', '')

def _get_haval192_5(txt):
    data = convert_spaced_str(txt)
    req = requests.get(f'{hash_api_base_url}/haval192-5.json/' + data)
    return req.text.replace('"', '')

def _get_haval224_5(txt):
    data = convert_spaced_str(txt)
    req = requests.get(f'{hash_api_base_url}/haval224-5.json/' + data)
    return req.text.replace('"', '')

def _get_haval256_5(txt):
    data = convert_spaced_str(txt)
    req = requests.get(f'{hash_api_base_url}/haval256-5.json/' + data)
    return req.text.replace('"', '')



# print(get_md2(txt))
# print(get_md5(txt))
# print(get_md4(txt))
# print(get_sha1(txt))
# print(get_sha224(txt))
# print(get_sha256(txt))fgewf
# # print(get_ripemd128(txt))
# print(get_ripemd160(txt))
# # print(get_ripemd256(txt))
# # print(get_ripemd320(txt))
# # print(get_ripemd128(txt))
# print(get_whirlpool(txt))
# print(get_snefru(txt))
# print(get_snefru256(txt))
# print(get_adler32(txt))
# print(get_fnv132(txt))