def remove_duplicates(nums):
    Unique_num=[]
    
    if nums:
        # mydict={num:nums.count(num)for num in nums}
        for num in nums:
            if num not in Unique_num:
                Unique_num.append(num)       
    return Unique_num