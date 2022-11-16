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
n1 = Nilsimsa(data="i have a cow", algorithm=Algorithms.TRAN)
n2 = Nilsimsa(data="there is he")


# print(n2.digest)
# print(n2.hexdigest())
# # # print(dig2)
# print(n1.hexdigest())
# print(n2.hexdigest())
print(compare_digests(n1.hexdigest(), n2.hexdigest()))