#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#


# ########### Brute Force ######################
# Pattern: Two nested loops
# Time: O(n²)
# Space: O(1)
# ###############################################
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False


# ########### Sort + Check #####################
# Pattern: Sorting + Adjacent comparison
# Time: O(n log n)
# Space: O(1)*  (depends on sorting implementation)
# ###############################################
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True

        return False


# ########### Hash Set #########################
# Pattern: Hash Set / Seen elements
# Time: O(n) average
# Space: O(n)
# ###############################################
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_set = set()

        for num in nums:
            if num in hash_set:
                return True
            hash_set.add(num)

        return False
        
# @lc code=end

