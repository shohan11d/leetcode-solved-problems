#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start


# ########### Sorting ##########################
# Pattern: Sorting + Comparison
# Time: O(n log n)
# Space: O(n)*  (depends on sorting implementation)
# ###############################################
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)


# ########### Hash Map #########################
# Pattern: Frequency Counter / Hash Map
# Time: O(n)
# Space: O(n)
# ###############################################
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        return countS == countT


# @lc code=end

            

        
# @lc code=end

