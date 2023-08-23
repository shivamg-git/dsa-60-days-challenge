from collections import Counter

def counter(string_):
    counter = {}
    for s in string_:
        if s in counter:
            counter[s] +=1
        else:
            counter[s]=1
    print(counter)
# counter("asdfgfdswe")    

def check_anagram(s,t):
    if len(s) == len(t):
        s_counter = Counter(s)
        t_counter = Counter(t)
        sub = s_counter - t_counter
        if len(sub)==0:
            return True
        else:
            return False
    else:
        return False


print(check_anagram("asdsdf","dsasfd"))
print(check_anagram("asdsdf","dsasf"))