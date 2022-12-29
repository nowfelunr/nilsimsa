from nilsimsa import *
from algorithhms import *
import glob
from utils import *
import csv
from multiprocessing import Process
import time

file_path = "iot-sentinal"


header = ['iteration_no', 'algorithm_name', 'threshold_type', 'window_size', 'accumulator_size', 'gram_size', 'hash_value']

# print(get_pcap_files(file_path))
def export_hashes(data, file_name, file_no):
    print(f"File no {file_no} startted")
    
    
    csv_file_name = f'{file_name}.csv'
    csv_file =  open(csv_file_name, 'w')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(header)
    
    n_grams = [3,5,7,9] 
    accumlator_sizes = [16, 1024]
    window_sizes = [7]
    threshold_types = [                      
        ThresholdType.STANDARD_DEVIATION,
        ]

    # listed_algorithms = [
    #     Algorithms.MD2, Algorithms.MD5, Algorithms.MD4,
    #     Algorithms.SHA1, Algorithms.SHA224, Algorithms.SHA256,
    #     Algorithms.SHA384, Algorithms.SHA512, Algorithms.WHIRLPOOL,
    #     Algorithms.ADLER32, Algorithms.CRC32, Algorithms.FNV132, Algorithms.FNV1A32, Algorithms.FNV1A64, Algorithms.FNV164,
    #     Algorithms.MMH3
    #     ]

    listed_algorithms = [
        Algorithms.MD5
        ]


    iteration_no = 1
    csv_data = []
    for gram in n_grams:
        for acc_size in range(accumlator_sizes[0], accumlator_sizes[1], 16):
            for window_size in window_sizes:
                for threshold_type in threshold_types:
                    for algorithm in listed_algorithms:
                        print(f"\n------------------------Current Iteratiion: {iteration_no}------------------------")
                       
                        print(f"Algo = {algorithm.name}, Th Type = {threshold_type}, Window Size = {window_size}, Acc Size = {acc_size}, Gram Size = {gram}")
                        nil = Nilsimsa(accumulator_size = acc_size, algorithm = algorithm, window_size = window_size, threshold_type = threshold_type, data=data)
                        
                        
                        # print(f'Hash Value: {nil.hexdigest()}')
                        
                        current_data = [iteration_no, algorithm.name, threshold_type, window_size, acc_size, gram, nil.hexdigest()]
                        csv_data.append(current_data)
                        iteration_no += 1
                        print("--------------------------------------------------------------------------------------")
                        print(iteration_no)
                        # if iteration_no == 1:
                        # print(f'{file_name} - {iteration_no}')
                        # csv_writer.writerows(csv_data)
                        # csv_file.close()
                        # print(f"File no {file_no} finished")
                        # return

    csv_writer.writerows(csv_data)
    csv_file.close()

def main():
    # with open('iot-sentinal/IPMAC-22-14.pcap', 'rb') as f:
    #     d = f.read()
    #     export_hashes(data=d, file_name="test")
    
    # return
    pcap_files = get_pcap_files(file_path)
    all_processes = []
    file_no = 1
    for current_file in pcap_files:
        current_file_name = current_file.split("/")[1]
        current_file_name = current_file_name.split(".")[0]
        # print(current_file_name)
        with open(current_file, 'rb') as f:
            # nil = Nilsimsa(data=f.read(), algorithm=Algorithms.MD2)
            # print(nil.hexdigest())
            data=f.read()
            # export_hashes(data=data, file_name=f'exported-hashes/{current_file_name}')

            p = Process(target=export_hashes, args=(data, f'exported-hashes/{current_file_name}',file_no))
            all_processes.append(p)
            file_no += 1 

    for pro in all_processes:
        pro.start()
    
    for pro in all_processes:
        pro.join()
    # pcap_files = get_pcap_files(file_path)
    # with open(pcap_files[0], 'rb') as f:
    #     data = f.read()
    #     print(data)
    #     export_hashes(data=data)


if __name__ == "__main__":
    start_time = time.time()

    main()

    print("--- %s seconds ---" % (time.time() - start_time))


