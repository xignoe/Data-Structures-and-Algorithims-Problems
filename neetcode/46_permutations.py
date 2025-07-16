class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start: int):
            # Base case: If start index reaches the length of nums, we've formed a permutation
            if start == len(nums):
                result.append(nums[:])  # Make a copy of nums and add to result
                return
            
            # Iterate over the array, swapping the start element with each element in the array
            for i in range(start, len(nums)):
                # Swap the current element with the start element
                nums[start], nums[i] = nums[i], nums[start]
                
                # Recursively generate permutations for the remaining elements
                backtrack(start + 1)
                
                # Backtrack to restore the original array for the next iteration
                nums[start], nums[i] = nums[i], nums[start]
        
        result = []
        backtrack(0)  # Start the backtracking process from index 0
        return result
