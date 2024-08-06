'''
Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.


'''


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split(" ")
        s = [x for x in s if x !=""]
        return len(s[-1])
    
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        words = s.split()
        return len(words[-1])
        