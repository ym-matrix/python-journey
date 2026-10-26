def check_nums(nums):
    result=[]
    idx=0
    while idx<len(nums) and nums[idx]!=7:
        result.append(nums[idx])
        idx+=1
        
    return result
print(check_nums([1,45,7,2,3,9]))