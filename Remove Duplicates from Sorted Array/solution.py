# link: https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/727/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        i = 0
        for j in range(1, len(nums)):

            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
                
        return i + 1

