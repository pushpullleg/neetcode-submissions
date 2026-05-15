class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        remove_dups = set(nums)
        #print(remove_dups)
        remove_dups_list = list(remove_dups)
        #print(remove_dups_list)
        sorted_list = sorted(remove_dups_list)
        #print(sorted_list)
        curr = sorted_list[0]
        length = len(sorted_list)
        seq = 1
        longest_seq = 0
        for i in range(1, length):
            #print(curr, sorted_list[i], seq)
            if sorted_list[i] == sorted_list[i - 1] + 1:
                seq += 1
            else:
                longest_seq = max(longest_seq, seq)
                seq = 1
        return max(longest_seq, seq)
