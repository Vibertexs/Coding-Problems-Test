'''
Given a list of integers sorted in ascending order nums,
square the elements and give the output in sorted order

Example 1
    Input
        nums = [-9, -2, 0, 2, 3]

    Output
        [0,4,4,9,81]

Example 2

Input
    nums = [1,2,3,4,5]

Output
    nums = [1,4,9,16,25]
'''

class Solution:
    def solve(self, nums):
        arr = []
        for i in(nums):
            arr.append(i**2)
        arr.sort()
        return arr

print(Solution().solve([-9, -2, 0, 2, 3]))
