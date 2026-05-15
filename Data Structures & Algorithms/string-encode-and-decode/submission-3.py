class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        print("result", res)
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        lis = []
        while(i < len(s)):
            j = i
            while s[j] != '#':
                j +=1
            length = int(s[i:j])
            extracted_str = s[j + 1:length + j + 1]
            lis.append(extracted_str)
            print("decoded :",extracted_str)
            i = length + j + 1
        return lis