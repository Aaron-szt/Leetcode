class Solution:
    def numUniqueEmails(self, emails):
        def preprocess(name):
            i = 0
            while i < len(name):
                if name[i] == '@':
                    return name
                elif name[i] == '.':
                    name = name[:i] + name[i+1:]
                    i -= 1
                elif name[i] == '+':
                    while name[i] != '@':
                        name = name[:i] + name[i+1:]
                        
                    return name
                i += 1
        
        ans = []
        for email in emails:
            add = preprocess(email)
            print(add)
            if add not in ans:
                ans.append(add)
        return len(ans)