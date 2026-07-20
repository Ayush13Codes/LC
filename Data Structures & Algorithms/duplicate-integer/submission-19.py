class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # T: O(n), S: O(n)
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
