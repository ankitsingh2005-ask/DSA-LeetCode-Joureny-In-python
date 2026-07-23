class Solution:

    def fun(self,n):
        sum_n = 0
        while n > 0:
            d = n % 10
            n = n // 10

            sum_n = sum_n + d * d
        return sum_n



    def isHappy(self, n: int) -> bool:

        slow = fast = n

        while fast != 1:
            slow = self.fun(slow)
            fast = self.fun(fast)
            fast = self.fun(fast)

            if slow == fast and slow != 1:
                return False

        fast = 1 

        return True 


#--------------main program------------------

if __name__ == "__main__":
    solution = Solution()
    n = 19

    res=solution.fun(n)
    print(solution.isHappy(n))
    print(res)