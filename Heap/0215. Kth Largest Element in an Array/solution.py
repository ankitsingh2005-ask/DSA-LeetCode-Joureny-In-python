import heapq

class Solution:
    def kthLargest(self, nums, k):

        pq = []

        for i in range(k):
            heapq.heappush(pq, nums[i])


        for i in range(k, len(nums)):
            if nums[i] <= pq[0]:
                continue

            heapq.heappop(pq)
            heapq.heappush(pq, nums[i])

        return pq[0]

#--------------main program------------------

nums = [3,2,3,1,2,4,5,5,6]
k = 4

sol = Solution()

res = sol.kthLargest(nums, k)
print(res)