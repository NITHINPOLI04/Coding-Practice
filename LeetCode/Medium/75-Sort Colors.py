#LINk: https://leetcode.com/problems/sort-colors/

# LeetCode 75. Sort Colors
#Remarks: This uses Python’s built-in sort(), which has O(n log n) time complexity which is less efficient.
# Approach 1: Directly using sort() fuction
# Time: O(nlogn), Space: O(logn)
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h = 0
        citations.sort(reverse = True)
        for i in range(len(citations)):
            if citations[i] >= i + 1:
                h = i + 1
            else:
                break
        return h

------------------------------------------------------
#Remarks: The problem expects an O(n) one-pass solution using constant space, often known as the Dutch National Flag algorithm.
# Approach 2: Dutch National Flag algorithm
# Time: O(n), Space: O(1)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low, mid, high = 0, 0, len(nums) - 1
        
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:  
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
