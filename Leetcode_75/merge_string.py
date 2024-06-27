'''
Merge Strings Alternately


Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r

'''

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        i, j = 0, 0 
        while(i<len(word1) or j < len(word2)):
            if i < len(word1):
                result.append(word1[i])
            if j < len(word2):
                result.append(word2[j])
            i = i + 1
            j = j + 1
        return ''.join(result)