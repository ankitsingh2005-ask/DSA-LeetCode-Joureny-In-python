import heapq
from collections import Counter

class Pair:
    def __init__(self, first, second):
        self.first = first      # frequency
        self.second = second    # character

    def __lt__(self, other):
        return self.first > other.first


class Solution:
    def reorganizeString(self, s: str) -> str:

        freq = Counter(s)

        pq = []

        for ch, count in freq.items():
            curr = Pair(count, ch)   # IMPORTANT: count first
            heapq.heappush(pq, curr)

        ans = []

        prev = None

        while pq:

            p = heapq.heappop(pq)

            ans.append(p.second)

            # Decrease frequency
            p.first -= 1

            # Put previous character back
            if prev is not None and prev.first > 0:
                heapq.heappush(pq, prev)

            # Current becomes previous
            prev = p

        # Character still remaining -> impossible
        if prev is not None and prev.first > 0:
            return ""

        return "".join(ans)


#-------------------main program-----------------------
sol = Solution()

s = "aab"

res = sol.reorganizeString(s)
print(res)