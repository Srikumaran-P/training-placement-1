class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left = 2
        right = x
        if x == 0:
            return 0
        if x < 4:
            return 1

        while(left <= right):
            mid = left + int((right - left) / 2)

            if mid*mid == x:
                return mid
            elif mid*mid < x:
                left = mid + 1
            else:
                right = mid - 1
        
        return right
