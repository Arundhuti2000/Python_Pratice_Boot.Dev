
#HashMap Solution
# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         n = len(nums)
#         presentnums={}
#         for input in nums:
#             presentnums[input]=True
        
#         for i in range(n+1):
#             if presentnums.get(i,False) is not True:
#                 return i

#Math Solution
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        return n * (n + 1) // 2 - sum(nums)

