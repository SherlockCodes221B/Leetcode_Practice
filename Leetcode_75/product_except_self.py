'''
Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        a=[1]*n
        for i in range(n-2, -1, -1):
            a[i]=nums[i+1]*a[i+1]
        b=1
        for j in range(1,n):
            b*=nums[j-1]
            a[j]*=b
        return a