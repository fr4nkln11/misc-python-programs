if __name__ == '__main__':
    N = int(input())
    p_list = []
    for _ in range(N):
        inp = input().split(' ')

        cmd = inp[0]

        if cmd == 'insert':
            p_list.insert(int(inp[1]),int(inp[2]))
        elif cmd == 'print':
            print(p_list)
        elif cmd == 'remove':
            p_list.remove(int(inp[1]))
        elif cmd == 'append':
            p_list.append(int(inp[1]))
        elif cmd == 'sort':
            p_list.sort()
        elif cmd == 'pop':
            p_list.pop()
        elif cmd == 'reverse':
            p_list.reverse()
        
        