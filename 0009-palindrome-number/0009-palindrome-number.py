class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_dummy = str(x)
        ans =''
        for i in x_dummy:
            ans = i + ans
        if x_dummy == ans:
            return True
        else:
            return False