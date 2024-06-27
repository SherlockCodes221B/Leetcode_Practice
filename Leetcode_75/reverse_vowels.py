'''
Reverse Vowels of a String

Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1:
Input: s = "hello"
Output: "holle"

'''

class Solution:
    def reverseVowels(self, s: str) -> str:
        p1 = 0
        legstr = len(s) - 1 
        p2 = legstr
        s = list(s)
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        while p1 < p2:
            if s[p1] not in vowels:
                p1 += 1
            elif s[p2] not in vowels:
                p2 -= 1
            else:
                s[p1], s[p2] = s[p2], s[p1]
                p1 = p1 +1
                p2 = p2 -1
            
        return ''.join(s)