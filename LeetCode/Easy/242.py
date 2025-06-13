class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_count = defaultdict(int)
        if len(s) != len(t):
            return False
        for char in s:
                freq_count[char]+=1
        for char in t:
            if char in freq_count:
                freq_count[char]-=1
                if freq_count[char]<0: #jb tk -1 ni ata mtlb it will check for the whole string, we're not checking with zero because otherwise it will eliminate immediately without chcking the whole string
                    return False
            else:
                return False
        return True
        