class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s = ''.join(filter(str.isalnum, s))
        if len(s) == 0:
            return True 
        print(s)
        for i in range(0,len(s)):
            if s[-i-1] != s[i]:
                print(s[-i-1],s[i])
                return False
        return True
    
if __name__ == "__main__":
    solution = Solution()
    # Test cases
    print(solution.isPalindrome("race a car")) 
    print(solution.isPalindrome("aHa/;]")) 