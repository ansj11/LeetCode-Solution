class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lst = []
        d = {'(':')','[':']','{':'}'}
        n = len(s)
        for i in range(n):
            if s[i] in d.keys():
                lst.append(s[i])
            elif s[i] in d.values():
                if len(lst)==0 or d[lst[-1]]!=s[i]:
                    return False
                elif d[lst[-1]]==s[i]:
                    lst.pop()

        return len(lst)==0