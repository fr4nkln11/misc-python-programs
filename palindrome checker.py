def palindromeCheck(string: str) -> str:
    string_reverse = string[::-1]
    return string == string_reverse
        
while True:
    string = input(">")
    print(palindromeCheck(string))
