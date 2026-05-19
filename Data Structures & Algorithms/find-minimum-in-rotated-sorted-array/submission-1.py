class Solution:
    def findMin(self, nums: List[int]) -> int:
        # T: O(log n), S: O(1)
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])

            m = (l + r) // 2
            res = min(res, nums[m])

            if nums[m] >= nums[l]:
                # search R
                l = m + 1
            else:
                # search L
                r = m - 1

        return res