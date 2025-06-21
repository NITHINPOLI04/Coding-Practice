#LINk: https://leetcode.com/problems/sort-an-array/

# LeetCode 912. Sort an Array
# Time: O(nlogn), Space: O(n)

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(nums, start, mid, end):
            temp = []
            i = start
            j = mid + 1

            while i <= mid and j <= end:
                if nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    temp.append(nums[j])
                    j += 1

            while i <= mid:
                temp.append(nums[i])
                i += 1

            while j <= end:
                temp.append(nums[j])
                j += 1

            for k in range(len(temp)):
                nums[start + k] = temp[k]


        def mergeSort(nums, start, end):
            if start < end:
                mid = (start + end) // 2
                mergeSort(nums, start, mid)
                mergeSort(nums, mid + 1, end)
                merge(nums, start, mid, end)

        mergeSort(nums, 0, len(nums) - 1)
        return nums
