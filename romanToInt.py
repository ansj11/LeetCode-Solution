class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
		d = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
		res, i = 0,0
		for i in range(len(s)-1):
			cur,nxt = s[i],s[i+1]
			if nxt and d[cur]<d[nxt]:
				res -= d[cur]
			else:
				res += d[cur]
		res += d[s[-1]]
		return res