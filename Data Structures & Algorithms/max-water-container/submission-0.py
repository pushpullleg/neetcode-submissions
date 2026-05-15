class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        area = 0
        #for i in range(len(heights)):
        while l < r:
            height = min(heights[l], heights[r])
            width = r - l
            area = max(area, height * width)
            if heights[l] < heights[r]:
                l += 1
            elif heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
        return area
        