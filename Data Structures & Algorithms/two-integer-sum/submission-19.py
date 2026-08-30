class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # T: O(n), S: O(n)
        num_index = {}  
        # num -> index
        for i, n in enumerate(nums):
            d = target - n
            if d in num_index:
                return [num_index[d], i]
            num_index[n] = i
        return -1
