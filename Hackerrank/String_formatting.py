import re 

def conv(n):
    bins = re.sub(r'0b', r'', bin(n))
    octs = re.sub(r'0o', r'', oct(n))
    hexs = re.sub(r'0x', r'', hex(n))
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