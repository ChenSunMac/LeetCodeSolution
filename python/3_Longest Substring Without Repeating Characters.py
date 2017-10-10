# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 15:28:57 2017

@author: chens
"""

class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        start = maxLength = 0
        usedChar = {}
        
        for i in xrange(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)

            usedChar[s[i]] = i

        return maxLength

if __name__ == "__main__":
    assert Solution().lengthOfLongestSubstring("abceads") == 6