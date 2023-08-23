def valid_palindrom(string_:str)->bool:
    if len(string_) <= 1:
        return True
    
    s,e=0,len(string_)-1
    while s<e:
        if string_[s]==string_[e]:
            s+=1
            e-=1
        else:
            return False
    return True



# Test Case
print(valid_palindrom(""))
print(valid_palindrom("a"))
print(valid_palindrom("aa"))
print(valid_palindrom("aaa"))
print(valid_palindrom("bab"))
print(valid_palindrom("baab"))
print(valid_palindrom("paris"))
print(valid_palindrom("qwertyytrew"))
print(valid_palindrom("qwertyytrewq"))
print(valid_palindrom("xxxxsssxxxx"))