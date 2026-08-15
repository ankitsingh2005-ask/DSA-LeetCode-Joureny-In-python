class Solution:
    def allocation(self, arr, limit, stud):

        k = 1
        page = 0
        for i in range(len(arr)):
            if page + arr[i] <= limit:
                page = page + arr[i]

            else:
                k += 1

                if k > stud:
                    return False

        return True

    def findPages(self, arr, k):
        n = len(arr)

        if n < k:
            return -1

        low = max(arr)
        high = sum(arr)
        res = -1

        while low <= high:
            mid = (low + high)// 2

            if self.allocation(arr, mid, k):
                res = mid
                high = mid - 1

            else:
                low = mid + 1


        return res


#-----------------------main program-----------------------
if __name__ == "__main__":
    sol = Solution()
    arr = [12, 34, 67, 90]
    k = 2

    res = sol.findPages(arr, k)
    print(res)
                
