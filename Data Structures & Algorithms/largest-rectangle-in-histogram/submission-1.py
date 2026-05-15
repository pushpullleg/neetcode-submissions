class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] #index, value
        maxArea = 0
        for i in range(len(heights)):
            curr_idx = i
            #no matter what always append the new element 
            #if incoming is less than top, pop and then append but with updated index
            while stack and heights[i] <= stack[-1][1]:
                prev_idx, prev_height = stack.pop()
                maxArea = max(maxArea, prev_height * (i - prev_idx))
                curr_idx = prev_idx
            stack.append((curr_idx, heights[i]))
        print(stack)
        #iterate through rest of the stack to find any max area
        for i, h in stack:
            maxArea = max(maxArea, (len(heights)- i) * h)
        return maxArea


            
