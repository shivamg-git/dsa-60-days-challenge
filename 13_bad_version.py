BAD_VERSION = 30

def is_bad_version(num:int)->bool:
    """ check is version is bad or not """
    return True if num >= BAD_VERSION else False

def find_bad_version_util(start:int, end:int)->int:
    mid = start + (end-start)//2
    print(mid)

    """ True => left, False => right """
    mid_bad = is_bad_version(mid) 
    print(mid_bad)
    if mid_bad and mid-1>=0 and (not is_bad_version(mid-1)):
        print(f"ans={mid}")
        return mid
    
    if mid_bad:
        find_bad_version_util(start,mid-1)
    else:
        find_bad_version_util(mid+1,end)

def find_bad_version(num:int)->int:
    """binary search"""
    return find_bad_version_util(0,num)

print(find_bad_version(num=100))