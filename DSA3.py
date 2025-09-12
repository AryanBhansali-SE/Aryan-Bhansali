''' Contains Duplicate'''

class solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for x in nums:
            if x in seen:
                return True
            seen.add(x)
        return False    
    
    
print(solution().hasDuplicate([1, 2, 3, 1]))   # True (1 is duplicate)
print(solution().hasDuplicate([1, 2, 3, 4 ]))   # False (all unique)