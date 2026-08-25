class Solution:
    def fib(self, n):

        if n == 0:
            return 0
        if n == 1:
            return 1

        ans1 = self.fib(n-1)
        ans2 = self.fib(n-2)

        return ans1 + ans2

#------------------main program------------------

if __name__ == "__main__":
    sol = Solution()
    n = 4

    res = sol.fib(n)
    print(res)