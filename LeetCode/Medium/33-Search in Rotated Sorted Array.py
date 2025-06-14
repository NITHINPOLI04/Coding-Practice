#LINk: https://leetcode.com/problems/search-in-rotated-sorted-array/

# LeetCode 33. Search in Rotated Sorted Array
# Time: O(log n), Space: O(1)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1

        while (start <= end):
            mid = start + (end - start) // 2

            if nums[mid] == target:
                return mid
            if nums[start] <= nums[mid]:
                if nums[start] <= target and nums[mid] >= target:
                    end = mid -1
                else:
                    start = mid + 1
            else:
                if nums[mid] <= target and nums[end] >= target:
                    start = mid + 1
                else:
                    end = mid - 1
        
        return -1
