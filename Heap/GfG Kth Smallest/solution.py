import heapq

class Solution:
    def kthSmallest(self, arr, k):

        pq = []

        for i in range(k):
            heapq.heappush(pq, - arr[i])

        for i in range(k, len(arr)):
            if arr[i] >= -pq[0]:
                continue

            heapq.heappop(pq)
            heapq.heappush(pq, -arr[i])

        return -pq[0]

#----------------main program------------------
arr = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10]
k = 4

obj = Solution()

ans = obj.kthSmallest(arr, k)

print("Array:", arr)
print("K:", k)
print("Kth Smallest Element:", ans)