
from typing import List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        pattern_count = [0] * 26
        initial_count = [0] * 26
        result = []
        def char_to_index(c):
            return ord(c) - ord('a')
        for i in range(len(p)):
            pattern_count[char_to_index(p[i])] += 1
            initial_count[char_to_index(s[i])] += 1
        
        if pattern_count == initial_count:
            result.append(0)
            
        #Slide the window
        for i in range(len(p), len(s)):
            #Add character from right
            initial_count[char_to_index(s[i])] += 1
            #Remove character from left
            initial_count[char_to_index(s[i - len(p)])] -= 1
            if pattern_count == initial_count:
                result.append(i - len(p) + 1)
        return result
    
if __name__ == "__main__":
    solution = Solution()
    # Test cases
    print(solution.findAnagrams("cbaebabacd", "abc")) 
    print(solution.findAnagrams("abab", "ab"))         
    