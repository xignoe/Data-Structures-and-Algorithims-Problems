class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums, reverse=True)[:k]
        
    def add(self, val: int) -> int:
        # Binary search to find the correct position of val in nums
        left = 0
        right = len(self.nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.nums[mid] < val:
                right = mid - 1
            else:
                left = mid + 1
        
        # Insert val into the correct position
        self.nums.insert(left, val)
        
        # If the length of nums exceeds k, remove the smallest element
        if len(self.nums) > self.k:
            self.nums.pop()
        
        # Return the smallest element, which is the last element in nums
        return self.nums[-1]
