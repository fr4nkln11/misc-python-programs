import re 

def conv(n):
    bins = re.sub(r'0b',r'',str(bin(n)))
    octs = re.sub(r'0o',r'',str(oct(n)))
    hexs = re.sub(r'0x',r'',str(hex(n)))
    hexs = hexs.upper()
    
    return [str(n), octs, hexs, bins]

def print_formatted(number):
    ws = (len(conv(number)[3]))
    for i in range(1, number+1):
        for v in conv(i):
            print(v.rjust(ws, " "), end=" ")
        print("")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)