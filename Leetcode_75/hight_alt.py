'''
    Find the Highest Altitude

    Input: gain = [-5,1,5,0,-7]
    Output: 1
    Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.

'''


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        presum = 0
        maxi = 0
        for i in range(len(gain)):
            presum = presum + gain[i]
            if presum > maxi:
                maxi = presum
        return maxi