#Brute Force:
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         output = []
#         n = len(nums)
#         if n > 10000:
#             return []
#         else:
#             for i in range(n):
#                 for j in range(i+1, n):
#                     if (nums[i]+nums[j]== target):
#                         output.append(i)
#                         output.append(j)
#                         return output


#HashMaps
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            compliment = target - nums[i]
            if (compliment in seen):
                return seen.get(compliment), i
            else: 
                seen[nums[i]] = i