class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        lst = []
        for i in nums:
            if i not in lst:
                lst.append(i)
                count=0
                if nums.count(i)>(n/2):
                    return i
