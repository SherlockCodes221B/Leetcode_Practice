'''

Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.

nums = [4,4,1,3,1,3,2,2,5,5,1,5,2,1,2,3,5,4]
k = 2
o/p: 2
'''


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0 
        c = 0
        j = len(nums)-1
        while i < j:
            if nums[i] + nums[j] == k:
                c = c + 1
                i = i + 1
                j = j - 1
            elif nums[i] + nums[j] > k:
                j = j - 1
            else:
                i = i + 1
        return c