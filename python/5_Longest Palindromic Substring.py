# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 16:06:04 2017

@author: chens
"""

class Solution:
    # @return an integer
    def longestPalindrome(self, s):
        if len(s) == 0:
            return 0
        begin, end, maxdistance = 0, 1, 0
        length = len(s)
        for i in range(1, length):
            # if i is odd
            if i & 1 :
                left = i / 2
                right = left
            else :
                left = i / 2 - 1
                right = left + 1
            while (left >= 0) and (right < length) and (s[left] == s[right]):
                left -= 1
                right += 1
            left += 1
            right -= 1
            if right - left >maxdistance:
                maxdistance = right - left
                begin = left
                end = right
        return s[begin: end + 1]
    
    
if __name__ == "__main__":
    assert Solution().longestPalindrome("abaeads") == "aba"