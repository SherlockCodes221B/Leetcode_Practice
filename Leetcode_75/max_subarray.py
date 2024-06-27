'''
Maximum Average Subarray I

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

'''


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = cur = sum(nums[:k])
        for i in range(len(nums) - k):
            cur = cur - nums[i] + nums[i + k]
            if cur > max_sum:
                max_sum = cur
        return max_sum / k
