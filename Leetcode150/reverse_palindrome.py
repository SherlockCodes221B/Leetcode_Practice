'''
Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.



'''


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(x.lower() for x in s if x.isalpha() or x.isdigit())
        t  = s[::-1]        
        return s==t