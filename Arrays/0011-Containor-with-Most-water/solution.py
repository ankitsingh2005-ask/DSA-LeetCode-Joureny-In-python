class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Get the length of the height list
        n = len(height)
        l = 0
        r = n - 1
        max_area = 0
        
        # Use two pointers to find the maximum area
        while l < r:
            w = r - l
            h = min(height[l], height[r])
            a = w * h
            max_area = max(max_area, a)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area


# Example usage
if __name__ == "__main__":
    solution = Solution()

    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

    result = solution.maxArea(height)

    print("The maximum area is:", result)