class Solution:
    def firstUniqChar(self, s):
        letters='abcdefghijklmnopqrstuvwxyz'
        index=[]
        for l in letters:
            if s.count(l) == 1:
                index.append(s.index(l))
        return min(index) if len(index) > 0 else -1

#参考代码：
#def firstUniqChar(self, s):
    """
    :type s: str
    :rtype: int
    """
        
#    letters='abcdefghijklmnopqrstuvwxyz'
#    index=[s.index(l) for l in letters if s.count(l) == 1]
#    return min(index) if len(index) > 0 else -1