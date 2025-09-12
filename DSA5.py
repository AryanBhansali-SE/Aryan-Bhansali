''' Group Anagram'''


from typing import List, Dict
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Use char-count signature (26-length tuple) as hashable key (robust vs sorting).
        groups: Dict[tuple, List[str]] = defaultdict(list)

        for s in strs:
            freq = [0]*26   # make a 26-length array for a–z
            for ch in s:   # count chars
                freq[ord(ch) - ord('a')] += 1
            groups[tuple(freq)].append(s)  # convert list->tuple (hashable key)

        return list(groups.values())

    
    
    

print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))