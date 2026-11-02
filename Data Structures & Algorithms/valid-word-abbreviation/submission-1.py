
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        w, a = len(word), len(abbr)
        i, j = 0, 0

        while j < a:
            if abbr[j].isdigit():
                if abbr[j] == '0':
                    return False

                prefix = 0
                while j < a and abbr[j].isdigit():
                    prefix = prefix * 10 + int(abbr[j])
                    j += 1

                i += prefix

            else:
                if i >= w or abbr[j] != word[i]:
                    return False

                i += 1
                j += 1

            if i > w:
                return False

        return i == w
