#Insertion Sort is useful for small data sets


def insertion_sort(nums):
    
    for i in range(1,len(nums)):
        j=i
        while j>0 and nums[j-1]>nums[j]:
            temp = nums[j-1]
            nums[j-1]=nums[j]
            nums[j]=temp
            j-=1
    return nums