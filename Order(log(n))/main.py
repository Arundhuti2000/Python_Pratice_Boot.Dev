def binary_search(target, arr):
    low = 0
    arr.sort()
    high=len(arr)-1
    while(low<=high): 
        mid = (low+high)//2
        if(target>arr[mid]):
            low = mid+1
        elif(target<arr[mid]):
            high = mid-1
        else:
            return True
    return False
            