class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        if target in nums:
            while l <= r:
                m = (l + r) // 2

                if nums[m] > target:
                    r = m - 1

                elif nums[m] < target:
                    l = m + 1

                else:
                    return m

        else:
            while l <= r:
                m = (l + r) // 2

                if nums[m] > target:
                    r = m - 1

                elif nums[m] < target:
                    l = m + 1

            if nums[m] > target:
                return m

            if nums[m] < target:
                return m + 1

        return 0