class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch == ')':
                # Reverse everything since the last '('
                temp = []
                while stack[-1] != '(':
                    temp.append(stack.pop())

                # Remove '('
                stack.pop()

                # Add the reversed substring back
                stack.extend(temp)
            else:
                stack.append(ch)

        return ''.join(stack)