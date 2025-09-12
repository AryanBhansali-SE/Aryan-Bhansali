''' valid Anagram problem'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Step 1: Quick check → if lengths differ, cannot be anagrams.
        if len(s) != len(t):
            return False

        # Step 2: Count characters in both strings.
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        # Step 3: If both dicts match, they are anagrams.
        return countS == countT


# Test runs
print(Solution().isAnagram("anagram", "nagaram"))   # True
print(Solution().isAnagram("rat", "car"))           # False

            
         