
from nilsimsa.utils import TRAN, POPC
from algorithhms import *
import numpy as np
from itertools import combinations
import statistics as st
from all_hashes import get_hash
from utils import interpolate, is_null_byte

def is_iterable_non_string(obj):
        return hasattr(obj, '__iter__') and not isinstance(obj, (bytes, str))

class Nilsimsa(object):
    def __init__(self, accumulator_size = 256, algorithm = Algorithms.TRAN, window_size = 5, n_grams = 3, threshold_type = ThresholdType.MEAN, transformation_const = TRAN, trigram_random=[0,1,2,3,4,5,6,7], data = None):
       
        self._digest = None
        self.num_char = 0 
        self.accumulator_size = accumulator_size         
        self.acc = [0] * accumulator_size       
        self.window = []          
        self.trigram_randdom = trigram_random
        self.threshold_type = threshold_type
        self.digest_size = accumulator_size/8
        self.transformation_const = transformation_const
        self.algorithm = algorithm
        self.window_size = window_size
        self.n_grams = n_grams 

        # if accumulator_size / digest_size != 8:
        #     raise Exception("invalid accumulator to digest size error. accumulator_size should be 8 * digest size.")

        if data:
            if is_iterable_non_string(data):
                for chunk in data:
                    
                    self.process(chunk)
            elif isinstance(data, (bytes, str)):
                # if isinstance(data, bytes):
                #     data = data.decode('utf-8')
                #     data = data.rsplit('\x00')
                
                self.process(data)
                
    
            else:
                raise TypeError("Excpected string, iterable or None, got {}"
                                    .format(type(data)))


    
    def tran_hash(self, a, b, c, n):
        return ((self.transformation_const[(a+n)&255]^self.transformation_const[b]*(n+n+1))+self.transformation_const[(c)^self.transformation_const[n]]) & 255

    
    def update_accumulator(self, letters, rnd):
       
        if self.algorithm != Algorithms.TRAN:
            # print(letters)
            letters = [str(x) for x in letters]
            current_data = '' . join(letters)
            # current_data.replace("\\r\\n", '')
            # if '\x00' in current_data:
            #     return
            
            hash_val = get_hash(str(current_data), str(self.algorithm.name))
            int_hash_value = int(hash_val, 16)
            interpolated_value = interpolate(int_hash_value, self.algorithm.min_size, self.algorithm.max_size, 0, self.accumulator_size)
            self.acc[interpolated_value] += 1 
        else:
            self.acc[self.tran_hash(letters[0], letters[1], letters[2], rnd)] += 1

    
    def process(self, chunk):
      
        self._digest = None

        if isinstance(chunk, str):
            chunk = chunk.encode('utf-8')

        for char in chunk:
            self.num_char += 1 
            c = char
            if len(self.window) == 2:
                current_letters = [c, self.window[0], self.window[1]]    
                self.update_accumulator(current_letters, 0)  
                # self.acc[self.tran_hash(c, self.window[0], self.window[1], self.trigram_randdom[0])] += 1
            
            elif len(self.window) > 2:
                all_combinations = combinations(self.window, self.n_grams-1)

                for idx, combi in enumerate(all_combinations):
                    current_letters = [c]
                    current_letters.extend(combi)

                    # print(current_letters)
                    self.update_accumulator(current_letters, idx+1)

                

            # if len(self.window) > 2:
            #     com = combinations(self.window, 3)
            #     for co in com:
            #         print(co)

            #     self.acc[self.tran_hash(c, self.window[0], self.window[2], self.trigram_randdom[1])] += 1
            #     self.acc[self.tran_hash(c, self.window[1], self.window[2], self.trigram_randdom[2])] += 1
            # if len(self.window) > 3:          
            #     self.acc[self.tran_hash(c, self.window[0], self.window[3], self.trigram_randdom[3])] += 1
            #     self.acc[self.tran_hash(c, self.window[1], self.window[3], self.trigram_randdom[4])] += 1
            #     self.acc[self.tran_hash(c, self.window[2], self.window[3], self.trigram_randdom[5])] += 1
            #     self.acc[self.tran_hash(self.window[3], self.window[0], c, self.trigram_randdom[6])] += 1
            #     self.acc[self.tran_hash(self.window[3], self.window[2], c, self.trigram_randdom[7])] += 1

           
            if len(self.window) < self.window_size:
                self.window = [c] + self.window
            else:
                self.window = [c] + self.window[:self.window_size-2]
            # print(len(self.window))
            


    def calculate_threshold(self):
        if self.threshold_type == ThresholdType.MEAN:
            num_trigrams = 8 * self.num_char - 28

            return num_trigrams / 256.0
        
        if self.threshold_type == ThresholdType.MEDIAN:
            return np.median(self.acc)
        
        if self.threshold_type == ThresholdType.IQR:
            q75, q25 = np.percentile(self.acc, [75 ,25])
            iqr = q75 - q25
            return iqr
        
        if self.threshold_type == ThresholdType.STANDARD_DEVIATION:
            return np.std(self.acc)

        if self.threshold_type == ThresholdType.MODE:
            return st.mode(self.window)
        
        if self.threshold_type == ThresholdType.Q1:
            q75, q25 = np.percentile(self.acc, [75 ,25])
            return q75
        
        if self.threshold_type == ThresholdType.Q2:
            q75, q25 = np.percentile(self.acc, [75 ,25])
            return q25
        


    def compute_digest(self):
        # num_trigrams = 0
        # if self.num_char == 3:          
        #     num_trigrams = 1
        # elif self.num_char == 4:      
        #     num_trigrams = 4
        # elif self.num_char > 4:        
        #     num_trigrams = 8 * self.num_char - 28
        

        self.threshold = self.calculate_threshold()
        # print(self.threshold)

        # digest = [0] * self.digest_size
        digest2 = [0] * self.accumulator_size
        for i in range(self.accumulator_size):
            if self.acc[i] > self.threshold:
                # print(1 << (i & 7))
                digest2[i] = 1
                # digest[i >> 3] += 1 << (i & 7)     
        # print(digest2)
        pow = 7
        res = []
        curr_val = 0
        for i in range(self.accumulator_size):
            curr_val += (2**pow) * digest2[i]
            pow -= 1
            if pow == -1 :
                res.append(curr_val)
                curr_val = 0
                pow = 7
        # print(len(res))

        # # print(bin(digest[1]))



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
        # print(digest_1)
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

