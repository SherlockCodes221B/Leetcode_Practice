'''
Reverse Words in a String
Example 1:
Input: s = "the sky is blue"
Output: "blue is sky the"

'''

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        words.reverse()
        return  ' '.join(words)
