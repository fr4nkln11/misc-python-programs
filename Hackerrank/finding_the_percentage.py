if __name__ == '__main__':
    n = int(input())
    sm = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        sm[name] = scores
    query = input()
    
    average = sum(sm[query])/len(sm[query])
    
    ans = "{:.2f}".format(average)
    print(ans)