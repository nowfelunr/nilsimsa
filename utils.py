import glob
def interpolate(x, in_min, in_max, out_min, out_max):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)



def get_pcap_files(dirpath):
    all_pcap_files = []
    for file in glob.glob(f"{dirpath}/*.pcap"):
        all_pcap_files.append(file)
    

    return all_pcap_files

def is_null_byte(data):
    if b'\x00' in data:
        return True
    

    return False