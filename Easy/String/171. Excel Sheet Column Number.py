class Solution:
    def titleToNumber(self, s):
        s = s[::-1]
        result = 0
        for exp, char in enumerate(s):
            result += (ord(char) - 65 + 1) * (26 ** exp)
        return result

#看到一行版本，学习了
def titleToNumber(s):
    return sum((ord(char) - 64) * (26 ** exp) for exp, char in enumerate(s[::-1]))

#Map/Reducen版本，学习了用法，真的狠
def titleToNumber(self, s):
    return reduce(lambda x,y:x*26+y,map(lambda x:ord(x)-ord('A')+1,s))