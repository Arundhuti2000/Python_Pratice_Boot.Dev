def quick_sort(nums, low, high):
    if low<high:
        t=partition(nums, low,high)
        quick_sort(nums, low, t-1)
        quick_sort(nums, t+1, high)
    return nums


def partition(nums, low, high):
    pivot = nums[high]
    i=low-1
    
    for j in range(low,high):
        if nums[j]<pivot:
            i+=1
            temp = nums[i]
            nums[i]=nums[j]
            nums[j]=temp
            
    temp = nums[i+1]
    nums[i+1]= nums[high]
    nums[high]= temp
    return i+1
