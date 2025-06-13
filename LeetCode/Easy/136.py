class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        final=0
        for num in nums:
            final^=num
        return final
    

#Using Sets:
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen=set(nums)
        n=len(nums)
        return 2*(sum(seen))-sum(nums)
        return 0
    
#Using HashMap:
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen={}
        n=len(nums)
        for i in range (n):
            if nums[i] in seen:
                 seen[nums[i]]+=1
            else:
                seen[nums[i]]=1
        
        for j in range (n):
            if seen[nums[j]]==1:
                return nums[j]
        return 0