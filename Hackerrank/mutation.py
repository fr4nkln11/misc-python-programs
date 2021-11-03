def mutate_string(string, position, character):
    mod = list(string)
    mod[position] = character
    return ''.join(mod)



if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)