def two_sum(list_, target)->tuple:
    set_ = set(list_)
    for a in list_:
        if target-a in set_:
            return (a, target-1)
    return ()

list_ = [1, 25, 26 , 32, 2, 6, 67, 87 , 100]
print(two_sum(list_,101))
print(two_sum(list_,103))
print(two_sum(list_,1))