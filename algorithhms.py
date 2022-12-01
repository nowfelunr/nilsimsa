
class Algorithms:
    class MD5:
        name = "md5"
        min_size = 0
        max_size = 2**128

    class MD2:
        name = "md2"
        min_size = 0
        max_size = 2**128
    
    class MD4:
        name = "md4"
        min_size = 0
        max_size = 2**128

    class SHA1:
        name = "sha1"
        min_size = 0
        max_size = 2**160

    class SHA224:
        name = "sha224"
        min_size = 0
        max_size = 2**224

    class SHA256:
        name = "sha256"
        min_size = 0
        max_size = 2**256
    
    class SHA384:
        name = "sha384"
        min_size = 0
        max_size = 2**384
    
    class SHA512:
        name = "sha512"
        min_size = 0
        max_size = 2**512
    
    class RIPEMD128:
        name = "ripemd128"
        min = 0 
        max_size = 2**128
    
    class RIPEMD160:
        name = "ripemd160"
        min_size = 0
        max_size = 2**160
    
    class RIPEMD256:
        name = "ripemd256"
        min_size = 0
        max_size = 2**256
    
    class RIPEMD320:
        name = "ripemd320"
        min_size = 0
        max_size = 2**320
    
    class WHIRLPOOL:
        name = "whirlpool"
        min_size = 0
        max_size = 2**512
    
    class SNEFRU:
        name = "snefru"
        min_size = 0
        max_size = 2**128

    class SNEFRU256:
        name = "snefru256"
        min_size = 0
        max_size = 2**256

    class GOST:
        name = "gost"
        min_size = 0
        max_size = 2**256
    
    class ADLER32:
        name = "adler32"
        min_size = 0
        max_size = 2**32

    
    class CRC32:
        name = "crc32"
        min_size = 0
        max_size = 2**32

    class fnv132:
        name = "fnv132"
        min_size = 0
        max_size = 2**32
    
    class fnv164:
        name = "fnv64"
        min_size = 0
        max_size = 2**64
    

    # 'md2', 'md5', 'md4', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512', 'ripemd128', 'ripemd160', 'ripemd256', 
    # 'ripemd320', 'whirlpool', 'snefru', 'snefru256', 'gost', 'adler32', 'crc32', 'fnv132', 'fnv164', 'fnv1a_64', 
    # 'fnv1a_32', 'joaat', 'mmh3', 'dbj2', 'sdbm', 'pearson', 'haval128_3', 'haval160_3', 'haval192_3', 'haval224_3', 
    # 'haval256_3', 'haval128_4', 'haval160_4', 'haval192_4', 'haval224_4', 'haval256_4', 'haval128_5', 'haval160_5', 
    # 'haval192_5', 'haval224_5','haval256_5'
    TRAN = "tran"
    # MD5 = "md2"
    # SHA2 = "md5"
class ThresholdType:
    MEAN = "mean"
    MEDIAN = "median"
    IQR = "iqr"
    Q1 = "Q1"
    Q2 = "Q2"
    STANDARD_DEVIATION = "std"
    MODE = "mode"