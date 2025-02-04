class Solution(object):
    # int => boolean
    # replace number by sum of squares of digits until number equals 1 and stays that way - or keeps going and never hits 1
    # positive integers, >= 1

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # while loop breaks if we reach 1, or if we reach 4 in which case we know its repeating
        while n:
        #sum of digits squared - 
            if n == 1:
                return True
            if n == 4:
                return False
            newNum = 0
            for i in range(len(str(n))):
                digit = (n // 10 ** i) % 10
                newNum += digit*digit
            n = newNum
        
        return
    

    #ex 19 => true
        # 1 + 81 = 82 -- 4 + 64 = 68 -- 36 + 64 = 100 -- 1 + 0 + 0 = 1
    #ex 2 => false
        # 4 16 -- 1 + 36 = 37 -- 9 + 49 = 58 -- 25 + 64 = 89 -- 64 + 81 = 145 - 1 + 16 + 25 = 42 -- 16 + 4 = 20
    #ex 1 => true
    #ex 3 => 9 81 65 61 37 58 89 145 42 20 4
    #ex 4 => 16 
        
