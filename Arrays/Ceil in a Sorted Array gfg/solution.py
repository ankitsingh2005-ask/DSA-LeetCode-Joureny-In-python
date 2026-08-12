class Solution:
    def findCeil(self, arr, x):

        low = 0
        high = len(arr) - 1
        res = -1

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] < x:
                low = mid + 1

            else:

                res = mid 
                high = mid - 1

        return res 

#----------------------main program--------------------
if __name__ == "__main__":
    sol = Solution()
    arr = [1, 2, 8, 10, 11, 12, 19]
    x = 5

    res = sol.findCeil(arr, x)

    print(res)