class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()
        l = r = 0
        while r < len(nums):
# if incoming number is greater than the last element, then keep popping
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            q.append(r)
# whenever the left pointer is out of bounce of the window, pop 1st element
            if l > q[0]:
                q.popleft()
#append the 1st element to the result, and then move one pointer
            if r + 1 >= k:
                res.append(nums[q[0]])
                l += 1
        # no matter what move the right pointer
            r += 1
            
        return res
            

        