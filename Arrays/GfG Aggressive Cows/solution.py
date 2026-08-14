class Solution:
    
    def placeAt(self, arr , k, mid):
        cow = 1
        pos = arr[0]
        
        for i in range(len(arr)):
            dist = arr[i] - pos
            if dist < mid:
                continue
            cow += 1
            pos = arr[i]
            
            if cow >= k:
                return True
            
        return False
            
    def aggressiveCows(self, arr, k):
        # code here
        n = len(arr)
        arr.sort()
        low = 1
        high = arr[n-1] - arr[0]
        res = -1
        
        while low <= high:
            mid = (low + high)// 2
            
            if self.placeAt(arr,k, mid):
                res = mid
                low = mid + 1
            else:
                high = mid - 1
                
        return res



#----------------------main program-------------------
if __name__ == "__main__":
    sol = Solution()
    arr = [10, 1, 2, 7, 5]
    k = 3
    res = sol.aggressiveCows(arr, k)
    print(res)