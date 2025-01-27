# problem: longest palindrome
# ref: https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
            TC: O(N^2)
            SC: O(1)
        """
        longest = ""
        # O(N)
        for idx, c in enumerate(s):
            i, j, palindrome = idx, idx, c
            # odd O(N)
            while i > 0 and j < len(s)-1:
                i -= 1
                j += 1
                if s[i] == s[j]:
                    palindrome = s[i] + palindrome + s[j]
                else:
                    break
            if len(palindrome) > len(longest):
                longest = palindrome

            i, j, palindrome = idx-1, idx, ""
            # even O(N)
            while i >= 0 and j <= len(s)-1:
                if s[i] == s[j]:
                    palindrome = s[i] + palindrome + s[j]
                else:
                    break
                i -= 1
                j += 1
            if len(palindrome) > len(longest):
                longest = palindrome
        return longest
