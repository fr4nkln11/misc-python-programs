if __name__ == "__main__":
    tc = int(input())
    uids = []
    for _ in range(tc):
        uids.append(input())
    uc = "QWERTYUIOPASDFGHJKLZXCVBNM"
    dig = "1234567890"
    an = uc + dig + "qwertyuiopasdfghjklzxcvbnm"
    
    def validate(uid):
        #rules
        if len(uid) != 10:
            return False
        elif len(set(uid)) != len(uid):
            return False

        digs = []
        ucs = []
        for char in uid:
            if char in dig:
                digs.append(char)
            if char in uc:
                ucs.append(char)
            if char not in an:
                return False

        if len(digs) < 3:
            return False
        if len(uc) < 2:
            return False
                    
                    
    for id in uids:
        v = validate(id)
        if v == False:
            print('Invalid')
        else:
            print('Valid')