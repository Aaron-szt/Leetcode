class Solution(object):
    def movesToStamp(self, stamp, target):
        ans = []
        tl = list(target)
        sl = list(stamp)
        def tool(i):
            flag = False
            # one by one compare the chars in target to those in stamps
            for j in range(len(stamp)):
                if tl[i + j] == '*':
                    continue
                if tl[i + j] != sl[j]:
                    return False
                flag = True
            if flag:
                ans.append(i)
                tl[i : i + len(stamp)] = ['*'] * len(stamp)
            return flag
            
        flag = True
        while flag:
            flag = False
            for i in range(len(target) - len(stamp) + 1):
                flag = tool(i) or flag
        
        print(tl, ans)
        if tl != ['*'] * len(target):
            return []
        return ans[::-1]