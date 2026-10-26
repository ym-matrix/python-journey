def check_nums(nums):
    # Collect numbers until the value 7 is reached
    result = []
    idx = 0
    while idx<len(nums) and nums[idx]!=7:
        result.append(nums[idx])
        idx += 1
        
    return result

# Example: return the values before the first 7
print(check_nums([1,45,7,2,3,9]))