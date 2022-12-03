
def validate(string, condition):
    for fail, i in enumerate(string, start=1):
        if eval(f"'{i}'.{condition}()") == True:
            return True
        #print(fail)
        if fail == len(string):
            return False
 
conditions = "isalnum isalpha isdigit islower isupper"

if __name__ == '__main__':
    s = str(input())
    for c in conditions.split(" "):
        print(validate(s,c))
       
# Alternative solution
"""
methods = [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper]

if __name__ == '__main__':
    s = str(input())
    for m in methods:
        print(any(m(c) for c in s))
"""