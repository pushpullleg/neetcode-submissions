class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l, r = 0, len(height) - 1
        res = 0
        maxleft = height[l]
        maxright = height[r]
        while l < r:
            print(l, r, maxleft, maxright, height[l], res)
            if maxleft <= maxright:
                if maxleft - height[l] > 0:
                    res += maxleft - height[l]
                l += 1
                maxleft = max(maxleft, height[l])
            else:
                if maxright - height[r] > 0:
                    res += maxright - height[r]
                r -= 1
                maxright = max(maxright, height[r])
            
        return res


        