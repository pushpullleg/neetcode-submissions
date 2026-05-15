class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        #1st loop for slow & fast pointer
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow2 = 0
        #2nd loop for slow1 & slow2 pointer
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                break
#can return slow or slow2 because thats where they intersect
        return slow


        