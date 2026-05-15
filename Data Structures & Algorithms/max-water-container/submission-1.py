class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        res = 0
        while l <= r:
            # area = l * b 
            h = min(heights[l], heights[r]) 
            b = r - l
            area = h * b
            res = max(res, area)
            if heights[l] < heights[r]:
                l = l + 1
            else:
                r = r - 1
        return res

        