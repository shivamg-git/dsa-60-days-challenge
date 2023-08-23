def binary_search_util(list_:list, target:int, s:int, e:int):
    if e<s:
        return -1
    
    mid = s + (e-s)//2
    if target == list_[mid]:
        return mid
    left = binary_search_util(list_, target, s, mid-1)
    right = binary_search_util(list_, target, mid+1,e )
    return left if left > right else right


def binary_search(list_:list, target:int) -> int:
    len_list = len(list_)
    if len_list == 0 :
        return -1

    return binary_search_util(list_,target,0,len_list-1)

print(binary_search([],1))
print(binary_search([1],1))
print(binary_search([1,2,3],3))
print(binary_search([1,2,3,4],4))
print(binary_search([1,2,3,4,5,6,7,8,9],10))