#mukesh1st attempt
class Solution:
    def isValid(self, s: str) -> bool:
        my_list = []
        my_dict = { ')':'(', ']':'[', '}' : '{' }

        for c in s:
            if my_list and c in my_dict:
                if my_list[-1] == my_dict[c]:
                    my_list.pop()
                else:
                    return False 
            else:
                my_list.append(c)
        if my_list == []: return True
        else : return False
        