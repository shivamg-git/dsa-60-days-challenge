from collections import Counter

def longest_palindrom(string_:str)->int:
    counter_ = Counter(string_)
    result = 0
    for key in counter_.keys():
        result          += 2*(counter_[key]//2)
        counter_[key]    = 0 if counter_[key]%2==0 else 1
    print(counter_)
    for key in counter_.keys():
        if counter_[key]==1:
            result+=1
            break
    return result

string_="aabbccd"
string_2="aabbccdd"
print(longest_palindrom(string_))
print(longest_palindrom(string_2))