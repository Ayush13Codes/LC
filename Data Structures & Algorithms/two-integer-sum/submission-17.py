class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # T: O(n), S: O(n)
        num_idx = {}  # num -> index

        for i, n in enumerate(nums):
            d = target - n
            if d in num_idx:
                return [num_idx[d], i]
            num_idx[n] = i
        return -1
