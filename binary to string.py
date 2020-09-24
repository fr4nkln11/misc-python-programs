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
    
    
while True:
    str = input()
    sb = string_bin(str)
    print(sb)
    print(bin_string(sb))