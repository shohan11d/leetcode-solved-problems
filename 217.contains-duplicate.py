#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         nums.sort()
#         for i in range(len(nums) - 1):
#             if nums[i] == nums[i + 1]:
#                 return True
#         return False

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_set = set()

        for num in nums:
            if num in hash_set:
                return True
            hash_set.add(num)
        return False
       
        
# @lc code=end

