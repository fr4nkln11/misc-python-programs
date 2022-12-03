uc = "QWERTYUIOPASDFGHJKLZXCVBNM"
lc = "qwertyuiopasdfghjklzxcvbnm"

def swap_case(s):
    mod = []
    for char in s:
        if char in uc:
            mod.append(lc[uc.index(char)])
        elif char in lc:
            mod.append(uc[lc.index(char)])
        else:
            mod.append(char)

    return "".join(mod)