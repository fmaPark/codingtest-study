def solution(nums):
    setofnums = set(nums)
    
    if (len(setofnums) > len(nums)/2):
        return len(nums)/2
    else:
        return len(setofnums)