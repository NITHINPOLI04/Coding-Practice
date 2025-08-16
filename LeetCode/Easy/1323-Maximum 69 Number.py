#LINk: https://leetcode.com/problems/maximum-69-number/

# LeetCode 1323. Maximum 69 Number
# Approach 1: Brute Force
# Time: O(n), Space: O(1)

class Solution:
    def maximum69Number (self, num: int) -> int:
        max_num = num
        str_num = list(str(num))
        for i in range(len(str_num)):
            if str_num[i] == '9':
                str_num[i] = '6'
            elif str_num[i] == '6':
                str_num[i] = '9'
            
            max_num = max(max_num, int("".join(str_num)))
            str_num = list(str(num))

        return max_num

#------------------------------------------------------

# Approach 2: Better Approach
# Time: O(n), Space: O(1)

class Solution:
    def maximum69Number (self, num: int) -> int:
        str_num = list(str(num))
        for i in range(len(str_num)):
            if str_num[i] == '6':
                str_num[i] = '9' 
                break
        return int("".join(str_num))
            hashmap[num] = i
