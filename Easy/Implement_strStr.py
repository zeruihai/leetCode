####### Online Solution ####### 83.28%

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        elif needle not in haystack:
            return -1
        elif needle in haystack:
            return haystack.index(needle)


####### Online Solution ####### 43.87%
class Solution:
	def strStr(self, haystack: str, needle: str) -> int:

		left = 0
		right = len(needle) - 1

		while right < len(haystack):

			if haystack[left:right + 1] == needle:
				return left

			left += 1
			right += 1

		return -1