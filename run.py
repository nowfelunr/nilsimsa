from nilsimsa import *
from algorithhms import *
# from nilsimsa.nil import *

# n1 = Nilsimsa(data="efewre 7ew8f 8w7e 78w74rer")
# freq = dict()
# for t in TRAN:
#     if t in freq:
#         freq[t] += 1
#     else:
#         freq[t] = 1

# print(len(freq))
# print(POPC[5])
# # n1 = Nilsimsa(data="i have a coedfewrewr werwe werf wetwer wertwer 4werewrw", threshold_type=ThresholdType.STANDARD_DEVIATION)
# # print(n1.hexdigest())
# # n2 = Nilsimsa(data="i have a coedfewrewr werwe werf wetwer wertwer 4werewrw", threshold_type=ThresholdType.MEAN)
# # print(n2.hexdigest())

# # n3 = Nilsimsa(data="i have a coedfewrewr werwe werf wetwer wertwer 4werewrw", threshold_type=ThresholdType.IQR, window_size=4)
# # print(n3.hexdigest())
# n1 = Nilsimsa(data="i have a coedfewrewr werwe werf wetwer wertwer 4werewrw", algorithm=Algorithms.MD5, accumulator_size=1024)
# print(n1.hexdigest())
# n2 = Nilsimsa(data="rdkhggru4ihuti huirhtuirhtuihreuihtuierhtuiheruihtuierhtuierht", algorithm=Algorithms.MD5, accumulator_size=1024)
# # n2 = Nilsimsa(data="there is he")


# # print(n2.digest)
# print(n2.hexdigest())
# # # # print(dig2)
# # print(n1.hexdigest())
# # print(n2.hexdigest())
# print(compare_digests(n1.hexdigest(), n2.hexdigest()))

text = "The quick brown fox jumps over the lazy dog"

n_grams = [3,4,5,6,7,8,9,10] 
accumlator_sizes = [8, 1024]
window_sizes = [4,5,6,7,8,9,10]
threshold_types = [ThresholdType.MEAN, ThresholdType.MEDIAN, ThresholdType.MODE]

listed_algorithms = [Algorithms.MD2, Algorithms.MD5, Algorithms.SHA256]
iteration_no = 1
for gram in n_grams:
    for acc_size in range(accumlator_sizes[0], accumlator_sizes[1], 8):
        for window_size in window_sizes:
            for threshold_type in threshold_types:
                for algorithm in listed_algorithms:
                    print(f"\n------------------------Current Iteratiion: {iteration_no}------------------------")
                    iteration_no += 1
                    print(f"Algo = {algorithm.name}, Th Type = {threshold_type}, Window Size = {window_size}, Acc Size = {acc_size}, Gram Size = {gram}")
                    nil = Nilsimsa(accumulator_size = acc_size, algorithm = algorithm, window_size = window_size, threshold_type = threshold_type, data=text)
                    print(f'Hash Value: {nil.hexdigest()}')
                    print("--------------------------------------------------------------------------------------")

