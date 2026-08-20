from typing import List
import heapq


class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __lt__(self, other):
        if self.first != other.first:
            return self.first < other.first

        return self.second > other.second


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        f = {}

        for word in words:
            f[word] = f.get(word, 0) + 1

        pq = []

        for word, freq in f.items():

            curr = Pair(freq, word)

            if len(pq) < k:
                heapq.heappush(pq, curr)

            else:
                if curr.first > pq[0].first:
                    heapq.heappop(pq)
                    heapq.heappush(pq, curr)

                elif curr.first == pq[0].first and curr.second < pq[0].second:
                    heapq.heappop(pq)
                    heapq.heappush(pq, curr)

        res = []

        while pq:
            res.append(heapq.heappop(pq).second)

        return res[::-1]

#-----------------------main program----------------------
words = ["i","love","leetcode","i","love","coding"]
k = 2

sol = Solution()

res = sol.topKFrequent(words, k)
print(res)