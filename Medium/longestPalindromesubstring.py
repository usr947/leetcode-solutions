class Solution(object):
    def longestPalindrome(self, s):
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]

        res = ""
        for i in range(len(s)):
            # Odd length
            tmp = expand(i, i)
            if len(tmp) > len(res):
                res = tmp
            # Even length
            tmp = expand(i, i+1)
            if len(tmp) > len(res):
                res = tmp
        return res