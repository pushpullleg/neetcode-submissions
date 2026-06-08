class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
            
        max_area = 0
        n = len(height)
        
        # Step 1: Find the index of the highest bar in the entire array
        # This peak acts as a natural barrier for both sides
        max_peak_idx = 0
        for i in range(1, n):
            if height[i] > height[max_peak_idx]:
                max_peak_idx = i

        # Step 2: Left-to-Right Sweep (Stopping at the max peak)
        l = 0
        while l < max_peak_idx:
            if height[l] == 0:
                l += 1
                continue

            r = l + 1
            area = 0
            while r <= max_peak_idx and height[l] > height[r]:
                area += (height[l] - height[r])
                r += 1

            max_area += area
            l = r

        # Step 3: Right-to-Left Sweep (Stopping at the max peak)
        r = n - 1
        while r > max_peak_idx:
            if height[r] == 0:
                r -= 1
                continue

            l = r - 1
            area = 0
            while l >= max_peak_idx and height[r] > height[l]:
                area += (height[r] - height[l])
                l -= 1

            max_area += area
            r = l

        return max_area