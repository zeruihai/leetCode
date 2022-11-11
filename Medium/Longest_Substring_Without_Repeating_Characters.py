from re import L
from turtle import right
from unittest.util import _MAX_LENGTH

####### My Solution ####### 65.47%
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        left = s[0]
        right = s[0]
        l = []
        l.append(left)
        tmp_len = 1
        max_len = 1
        for i in range(1, len(s)):
            right = s[i]
            if right not in l:
                l.append(right)
                tmp_len += 1
            else:
                while l[0] != right:
                    l.pop(0)
                l.pop(0)
                l.append(right)
                tmp_len = len(l)

            if tmp_len > max_len:
                max_len = tmp_len

        return max_len

####### Online Solution ####### 85.73%

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen = ''
        mx = 0
		#1. for each character in s
        for c in s:
			#2. check if c is seen
            if c not in seen:
			#3. if not seen, add to seen list 
                seen+=c
            #4 if seen, slice seen list to previous c
            # for example, if c is 'a' and seen list is 'abc'
            # you will be slicing previous 'a'(seen.index(c)+1), thus seen list become 'bc'
            # then add the current 'a' bc + a, seenlist = 'bca'
            else:
                seen = seen[seen.index(c) + 1:] + c
            #5 check max length between current max with new length of seen
            mx = max(mx, len(seen))
        return mx