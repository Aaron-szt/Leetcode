#Mie HaHaHa! 96.63%!!!
class Solution:
    def rotateString(self, A, B):
        if len(A) != len(B):
            return False
        A += A
        return B in A

