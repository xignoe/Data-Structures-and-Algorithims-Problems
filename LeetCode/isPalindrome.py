class Solution:
    def isPalindrome(self, x: int) -> bool:
        original = x
        backwards = 0
        
        while x > 0:
            backwards = (backwards * 10) + (x % 10)
            x = x // 10
            
        return original == backwards