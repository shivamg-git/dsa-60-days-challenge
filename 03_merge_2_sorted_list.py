def merge_2_sorted_list(list_1,list_2)->list:
    len_1 = len(list_1)
    len_2 = len(list_2)
    list_ = []

    i,j=0,0
    while i<len_1 and j<len_2:
        if list_1[i] <= list_2[j]:
            list_.append(list_1[i])
            i+=1
        else:
            list_.append(list_2[j])
            j+=1
    if i<len_1:
        list_.extend(list_1[i:])
    else:
        list_.extend(list_2[j:])
    
    return list_


list_1 = [1,3,5,7,9]
list_2 = [2,3,4,5,6,7,8,9]
print(merge_2_sorted_list(list_1,list_2))
