# Given a binary tree, find its height.


#User function Template for python3

'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
        '''
class Solution:
    #Function to find the height of a binary tree.
    def height(self, root):
        # code here
        if root is  None:
            return 0
        else:
            leftd = self.height(root.left)
            rightd = self.height(root.right)
        return 1 + max(leftd,rightd)
