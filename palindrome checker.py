def palindromeCheck(string: str) -> str:
    string_reverse = string[::-1]
    if string == string_reverse:
        return True
    else:
        return False
        
while True:
    string = input(">")
    print(palindromeCheck(string))
