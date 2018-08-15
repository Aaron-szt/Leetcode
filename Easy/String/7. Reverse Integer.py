class Solution:
    def reverse(self, x):
        exp = 0
        y = 0
        if x < 0:
	        xx = -x
        else:
        	xx = x
        while xx // 10 != 0:
            xx = xx // 10
            exp += 1

        if x < 0:
        	xx = -x
        else:
        	xx = x
        while xx // 10 != 0:
            y += xx % 10 * 10 ** exp
            xx = xx // 10
            exp -= 1

        y += xx % 10 * 10 ** exp

        if x < 0:
        	return -y if -y > -2**31 else 0
        else:
        	return y if y < 2**31-1 else 0
                
#网上代码真的狠
def reverse(self, x):
    s = cmp(x, 0)
    r = int(`s*x`[::-1])
    return s*r * (r < 2**31)