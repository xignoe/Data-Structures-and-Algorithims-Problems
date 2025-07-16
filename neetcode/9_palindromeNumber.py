class Solution:
    def isPalindrome(self, x: int) -> bool:
        p = str(x)
        isP = ""
        count = len(p)
        while count > 0:
            isP += p[count - 1]
            count -= 1
        print("p", p)
        print("isP", isP)

        if (p == isP):
            return True
        else:
            return False