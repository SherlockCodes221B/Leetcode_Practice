'''

Input: names = ["Mary","John","Emma"], heights = [180,165,170]
Output: ["Mary","Emma","John"]
Explanation: Mary is the tallest, followed by Emma and John.

'''
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        res = [y for x,y in sorted(zip(heights, names), reverse=True)]
        return res
        