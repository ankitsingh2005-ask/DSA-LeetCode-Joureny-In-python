class Solution:
    def maxSubarraySum(self, arr, k):
        # code here 
        low = 0
        high = k - 1
        
        window_sum = 0
        
        for i in range(low, high + 1):
            window_sum += arr[i]
            
        res = window_sum
        
        while high < len(arr):
            res = max(res, window_sum)
            low += 1
            high += 1
            window_sum = window_sum - arr[low - 1]
            
            if high == len(arr):
                break
            
            window_sum = window_sum + arr[high]
            
        return res


#-------------main program---------------------------------------

if __name__ == "__main__":
    solution = Solution()
    arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
    k = 4

    result = solution.maxSubarraySum(arr, k)
    print(result)
            
            
            
            
        
        