def wrap(string, max_width):
    wrapped = []
    count = 0
    
    for c in string:
        count += 1
        wrapped.append(c)
        if count == max_width:
            wrapped.append("\n")
            count = 0

    return "".join(wrapped)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)