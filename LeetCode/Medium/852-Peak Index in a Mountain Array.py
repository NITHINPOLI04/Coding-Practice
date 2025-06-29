#LINk: https://leetcode.com/problems/peak-index-in-a-mountain-array/

# LeetCode 852. Peak Index in a Mountain Array
# Time: O(logn), Space: O(1)

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 1, len(arr) - 2

        while(left <= right):
            mid = left + (right - left) // 2

            if arr[mid - 1] < arr[mid] and arr[mid] > arr[mid + 1]:
                return mid
            elif arr[mid - 1] < arr[mid]:
                left = mid + 1
            else:
                right = mid - 1

        return -1
