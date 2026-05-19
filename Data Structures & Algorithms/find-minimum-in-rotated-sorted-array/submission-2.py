class Solution:
    def findMin(self, nums: List[int]) -> int:
        # T: O(log n), S: O(1)
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            # If array is already sorted
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = (l + r) // 2
            res = min(res, nums[m])

            if nums[m] >= nums[l]: # Search R
                l = m + 1
            else:
                r = m - 1

        return res
