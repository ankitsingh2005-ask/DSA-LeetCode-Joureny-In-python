class Solution:
    def smallestSumSubarray(self, A, N):
        
        #Your code here
        best_ending = A[0]
        ans = A[0]
        
        for i in range(1, len(A)):
            v1 = best_ending + A[i]
            v2 = A[i]
            
            best_ending = min(v1,v2)
            
            ans = min(ans, best_ending)
            
        return ans

#---------------main Program--------------------

if __name__ == "__main__":
    solution = Solution()
    A = [3,-4, 2,-3,-1, 7,-5]
    N = 7
    res = solution.smallestSumSubarray(A,N)

    print(res)