# convert input String to Binary and vice versa
import re

def string_bin(string):
    string = string.split(' ')
    bins = list(map(lambda x: ' '.join(bin(ord(i)) for i in x), string))
    bins = ' . '.join(bins)
    bins = re.sub(r'0b',r'',bins)
    return bins

def bin_string(binseq):
    binseq = binseq.replace(' . ', ' ')
    binseq = binseq.split(' ')
    string = ''.join(chr(int(i, 2)) for i in binseq)
    return string
    
if __name__ == "__main__":
    while True:
        print("type sb to convert string to binary")
        print("type bs to convert binary to string")
        
        choice = input(': ')
        if choice == "sb":
            string = input("input the string you wish to convert: ")
            print(f"\nBinary: {string_bin(string)}\n")
        elif choice == "bs":
            bin = input("input the binary sequence you wish to convert: ")
            print(f"\nString: {bin_string(bin)}\n")