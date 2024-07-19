'''
Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

'''

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        checker = 0
        for n in nums:
            if checker < 0:
                return False
            elif n > checker:
                checker = n
            checker -= 1
            
        return True