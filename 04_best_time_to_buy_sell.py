def best_time_to_buy_sell(list_:list)->int:
    s,e=0,len(list_)-1
    best_buy    = None
    best_sell   = None
    while s<e:
        if best_buy:
            if best_buy > list_[s]:
                best_buy=list_[s]
        else:
            best_buy=list_[s]
        
        if best_sell:
            if best_sell < list_[e]:
                best_sell=list_[e]
        else:
            best_sell=list_[e]
        s+=1
        e-=1

    if best_buy and best_sell:
        return best_sell - best_buy if best_sell> best_buy else 0
    return 0

# Driver
print(best_time_to_buy_sell([1,2,3,4,5,6,7,8]))
print(best_time_to_buy_sell([]))
print(best_time_to_buy_sell([1]))
print(best_time_to_buy_sell([9,7,6,5,4,3,1]))
print(best_time_to_buy_sell([10,2,30,4,5,60,78,8]))