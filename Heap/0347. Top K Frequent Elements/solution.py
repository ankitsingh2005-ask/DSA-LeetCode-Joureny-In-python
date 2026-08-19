from typing import List
import heapq

class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __lt__(self, other):
        if self.first != other.first:
            return self.first < other.first
        return self.second < other.second

class Solution:
    def topKFrequent(self, nums, k):

        f = {}

        for num in nums:
            f[num] = f.get(num, 0) + 1

        pq = []

        for elem, freq in f.items():
            curr = Pair(freq, elem)

            if len(pq) < k:
                heapq.heappush(pq, curr)

            else:
                if curr.first > pq[0].first:
                    heapq.heappop(pq)
                    heapq.heappush(pq, curr)

        res = []

        while pq:
            res.append(heapq.heappop(pq).second)

        return res

#-----------------main program-------------------------

sol = Solution()
nums = [1,2,1,2,1,2,3,1,3,2]
k = 2

res = sol.topKFrequent(nums, k)

print(res)
