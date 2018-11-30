class Solution:
    def isLongPressedName(self, name, typed):
        i = 0
        if name == typed:
            return True
        elif len(name) == 0 and len(typed) != 0:
            return False
        else:
            while len(typed):
                if len(name) == 0:
                    return False
                if name[0] == typed[0]:
                    if len(name) == 1 and len(typed) > 1:
                        while name[0] == typed[0] and len(typed) > 1:
                            typed = typed[1:]
                    else:
                        name = name[1:]
                        typed = typed[1:]
                else:
                    typed = typed[1:]
            if len(name) == 0:
                return True
            else:
                return False 
                
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        