'''
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        strs.sort()
        first = strs[0]
        last = strs[-1]
        prefix = []
        for i in range(len(first)):
            if i < len(last) and first[i] == last[i]:
                prefix.append(first[i])
            else:
                break
        return "".join(prefix)