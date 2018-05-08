# Valid Parentheses

## 题目描述

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

## 解题思路

很常见的括号匹配问题，第一时间想到栈的用法。

Python 中可以借助于列表的 append()、pop() 方法来实现。

即如果列表为空或者不匹配，那么就压入栈，否则就弹出。

```python
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
```