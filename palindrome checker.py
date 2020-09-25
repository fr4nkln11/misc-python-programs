def palindromeCheck(string: str) -> str:
    string_reverse = string[::-1]
    if string == string_reverse:
        return True
    else:
        return False
        
if palindromeCheck("panap") == True:
    print("True")
else:
    print("False")