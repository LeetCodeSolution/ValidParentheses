class Solution:
    def match(self, s, t):
        """
        if match
        :param s: source
        :param t: target
        :return: match or not
        """
        if s == '{' and t == '}' or s == '[' and t == ']' or s == '(' and t == ')':
            return True
        return False
    
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in s:
            if len(stack) > 0 and self.match(stack[-1], i):
                stack.pop()
            else:
                stack.append(i)
        if len(stack) == 0:
            return True
        else:
            return False


str = input()
s = Solution()
result = s.isValid(str)
print(result)
