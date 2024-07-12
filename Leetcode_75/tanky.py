'''11. Container With Most Water
Solved
Medium
Topics
Companies
Hint
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        p1 = 0
        p2 = len(height)-1
        maxArea = 0
        while p1 < p2:
            currArea = min(height[p1], height[p2]) * (p2 - p1)
            maxArea = max(maxArea, currArea )
            if height[p1] < height[p2]:
                p1 = p1 + 1
            else:
                p2 = p2 - 1

        return maxArea 
