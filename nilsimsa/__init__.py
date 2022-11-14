
from nilsimsa.utils import TRAN, POPC


class Nilsimsa(object):
    def __init__(self, accumulator_size = 256, digest_size = 32, threshold = None, transformation_const = TRAN, trigram_random=[0,1,2,3,4,5,6,7], data = None):
       
        self._digest = None
        self.num_char = 0          
        self.acc = [0] * accumulator_size       
        self.window = []          
        self.trigram_randdom = trigram_random
        self.threshold = threshold
        self.digest_size = digest_size
        self.transformation_const = transformation_const


        if data:
            if isinstance(data, (bytes, str)):
                self.process(data)
            else:
                raise TypeError("Excpected string, iterable or None, got {}"
                                    .format(type(data)))

    def tran_hash(self, a, b, c, n):
        return ((self.transformation_const[(a+n)&255]^self.transformation_const[b]*(n+n+1))+self.transformation_const[(c)^self.transformation_const[n]]) & 255

    def process(self, chunk):
      
        self._digest = None

        if isinstance(chunk, str):
            chunk = chunk.encode('utf-8')

        for char in chunk:
            self.num_char += 1 
            c = char
            if len(self.window) > 1:     
               
                self.acc[self.tran_hash(c, self.window[0], self.window[1], self.trigram_randdom[0])] += 1
            if len(self.window) > 2:           
                self.acc[self.tran_hash(c, self.window[0], self.window[2], self.trigram_randdom[1])] += 1
                self.acc[self.tran_hash(c, self.window[1], self.window[2], self.trigram_randdom[2])] += 1
            if len(self.window) > 3:          
                self.acc[self.tran_hash(c, self.window[0], self.window[3], self.trigram_randdom[3])] += 1
                self.acc[self.tran_hash(c, self.window[1], self.window[3], self.trigram_randdom[4])] += 1
                self.acc[self.tran_hash(c, self.window[2], self.window[3], self.trigram_randdom[5])] += 1
                # duplicate hashes, used to maintain 8 trigrams per character
                self.acc[self.tran_hash(self.window[3], self.window[0], c, self.trigram_randdom[6])] += 1
                self.acc[self.tran_hash(self.window[3], self.window[2], c, self.trigram_randdom[7])] += 1

           
            if len(self.window) < 4:
                self.window = [c] + self.window
            else:
                self.window = [c] + self.window[:3]
            
            # print(self.window)


    def compute_digest(self):
        num_trigrams = 0
        if self.num_char == 3:          
            num_trigrams = 1
        elif self.num_char == 4:      
            num_trigrams = 4
        elif self.num_char > 4:        
            num_trigrams = 8 * self.num_char - 28
        

        if self.threshold is None:
            self.threshold = num_trigrams / 256.0

        digest = [0] * self.digest_size
        digest2 = [0] * 256
        for i in range(256):
            if self.acc[i] > self.threshold:
                # print(1 << (i & 7))
                digest2[i] = 1
                # digest[i >> 3] += 1 << (i & 7)     
        
        pow = 7
        res = []
        curr_val = 0
        for i in range(256):
            curr_val += (2**pow) * digest2[i]
            pow -= 1
            if pow == -1 :
                res.append(curr_val)
                curr_val = 0
                pow = 7
        # print(len(res))

        # print(bin(digest[1]))



        # self._digest = digest[::-1]   
        self._digest = res[::-1]

    @property
    def digest(self):
        if self._digest is None:
            self.compute_digest()
        return self._digest

    def hexdigest(self):
        return ''.join('%02x'%i for i in self.digest)

    def __str__(self):
        return self.hexdigest()

    def from_file(self, fname):
        f = open(fname, "rb")
        data = f.read()
        self.update(data)
        f.close()

    def compare(self, digest_2, is_hex = False):
        if is_hex:
            digest_2 = convert_hex_to_ints(digest_2)
        bit_diff = 0
        for i in range(len(self.digest)):
            bit_diff += POPC[self.digest[i] ^ digest_2[i]]          

        return 128 - bit_diff     

def convert_hex_to_ints(hexdigest):
    return [int(hexdigest[i:i+2], 16) for i in range(0, 63, 2)]

def compare_digests(digest_1, digest_2, is_hex_1=True, is_hex_2=True, threshold=None):
    if threshold is not None:
        threshold -= 128    
        threshold *= -1
    if is_hex_1 and is_hex_2:
        bits =  0
        print(digest_1)
        for i in range(0, 63, 2):
            bits += POPC[255 & int(digest_1[i:i+2], 16) ^ int(digest_2[i:i+2], 16)]
            if threshold is not None and bits > threshold: break
        return 128 - bits
    else:
        if is_hex_1:  digest_1 = convert_hex_to_ints(digest_1)
        if is_hex_2:  digest_2 = convert_hex_to_ints(digest_2)
        bit_diff = 0
        for i in range(len(digest_1)):
            bit_diff += POPC[255 & digest_1[i] ^ digest_2[i]]
            if threshold is not None and bit_diff > threshold: break
        return 128 - bit_diff

