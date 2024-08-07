'''
Given a sorted array arr[] of distinct integers. Sort the array into a wave-like array(In Place). In other words, arrange the elements into a sequence such that arr[1] >= arr[2] <= arr[3] >= arr[4] <= arr[5].....
If there are multiple solutions, find the lexicographically smallest one.

Note: The given array is sorted in ascending order, and you don't need to return anything to change the original array.

Examples:

Input: n = 5, arr[] = {1,2,3,4,5}
Output: 2 1 4 3 5
Explanation: Array elements after sorting it in the waveform are 2 1 4 3 5.

'''


class Solution:
    def convertToWave(self, n : int, arr : List[int]) -> None:
        # code here
        i = 0
        while i < n-1:
            j = i + 1
            arr[i],arr[j] = arr[j],arr[i]
            i = i + 2
        return arr