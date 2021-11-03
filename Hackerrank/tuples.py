if __name__ == "__main__":
    n = int(input())
    num_tuple = tuple(map(int,input().split(' ')))
    print(hash(num_tuple))