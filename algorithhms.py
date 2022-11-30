
class Algorithms:
    class MD5:
        name = "md5"
        min_size = 0
        max_size = 2**128
    # 'md2', 'md5', 'md4', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512', 'ripemd128', 'ripemd160', 'ripemd256', 
    # 'ripemd320', 'whirlpool', 'snefru', 'snefru256', 'gost', 'adler32', 'crc32', 'fnv132', 'fnv164', 'fnv1a_64', 
    # 'fnv1a_32', 'joaat', 'mmh3', 'dbj2', 'sdbm', 'pearson', 'haval128_3', 'haval160_3', 'haval192_3', 'haval224_3', 
    # 'haval256_3', 'haval128_4', 'haval160_4', 'haval192_4', 'haval224_4', 'haval256_4', 'haval128_5', 'haval160_5', 
    # 'haval192_5', 'haval224_5','haval256_5'
    TRAN = "tran"
    # MD5 = "md2"
    # SHA2 = "md5"

class AlgorithmSizes:
    MD5 = (0, 2**128)

class ThresholdType:
    MEAN = "mean"
    MEDIAN = "median"
    IQR = "iqr"
    Q1 = "Q1"
    Q2 = "Q2"
    STANDARD_DEVIATION = "std"
    MODE = "mode"