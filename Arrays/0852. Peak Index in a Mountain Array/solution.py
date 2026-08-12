class Solution:
    def peakInMountainArray(self, arr):

        low = 0
        high = len(arr) -1
        res = 0

        while low <= high:
            mid = (low + high) //2
            if arr[mid] < arr[mid + 1]:
                low = mid + 1

            else:
                res = mid
                high = mid -1 

        return res

#------------------------main program----------------

if __name__ == "__main__":
    sol = Solution()

    arr = [0,2,1,0]
    res = sol.peakInMountainArray(arr)
    print(res)