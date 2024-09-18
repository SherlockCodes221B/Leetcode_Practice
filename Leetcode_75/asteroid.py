'''
Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

'''


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while stack and stack[-1] > 0 > a:
                if stack[-1] < abs(a):
                    stack.pop()
                    continue
                elif stack[-1] == abs(a):
                    stack.pop()
                break # this means asteroid must be destroyed (not add to stack in else statement below)
            else:
                stack.append(a)
        
        return stack
