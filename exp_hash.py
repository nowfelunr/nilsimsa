from all_hashes import get_hash

listed_hasehs = [
    'md2', 'md5', 'md4', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512', 'ripemd128', 'ripemd160', 'ripemd256', 
    'ripemd320', 'whirlpool', 'snefru', 'snefru256', 'gost', 'adler32', 'crc32', 'fnv132', 'fnv164', 'fnv1a_64', 
    'fnv1a_32', 'joaat', 'mmh3', 'dbj2', 'sdbm', 'pearson', 'haval128_3', 'haval160_3', 'haval192_3', 'haval224_3', 
    'haval256_3', 'haval128_4', 'haval160_4', 'haval192_4', 'haval224_4', 'haval256_4', 'haval128_5', 'haval160_5', 
    'haval192_5', 'haval224_5','haval256_5'
    ]

for hs in listed_hasehs:

    print(get_hash(text="hello", hash_name=hs))