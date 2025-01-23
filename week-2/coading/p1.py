# ref: https://leetcode.com/problems/reverse-words-in-a-string

class Solution:
    def reverseWords(self, s: str) -> str:
        """
            SC: O(N) saving a word
            TC: O(N) iterating through all the characters in string s
        """
        if len(s) == 0:
            return ""
            
        output = ""
        word = "" # SC: O(N) -> at worst saving all the characters
        # O(N) -> iterate through all the characters in the string
        for c in s:
            if c == " " and len(word) > 0:
                output = word + " " + output
                word = ""
            if c == " " and len(word) == 0:
                pass
            if c != " ":
                word += c
        if len(word) > 0:
            output = word + " " + output
        return output[:-1]  # remove the tailing " "
