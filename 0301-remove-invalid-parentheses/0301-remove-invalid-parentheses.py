class Solution:
    def removeInvalidParentheses(self, s):
        result = set()

        def is_valid(string):
            count = 0

            for ch in string:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1

                    if count < 0:
                        return False

            return count == 0

        def backtrack(index, path, left_remove, right_remove):
            if index == len(s):
                if left_remove == 0 and right_remove == 0:
                    string = ''.join(path)

                    if is_valid(string):
                        result.add(string)
                return

            ch = s[index]

            if ch == '(' and left_remove > 0:
                backtrack(
                    index + 1,
                    path,
                    left_remove - 1,
                    right_remove
                )

            elif ch == ')' and right_remove > 0:
                backtrack(
                    index + 1,
                    path,
                    left_remove,
                    right_remove - 1
                )

            path.append(ch)

            backtrack(
                index + 1,
                path,
                left_remove,
                right_remove
            )

            path.pop()

        left_remove = 0
        right_remove = 0

        for ch in s:
            if ch == '(':
                left_remove += 1
            elif ch == ')':
                if left_remove > 0:
                    left_remove -= 1
                else:
                    right_remove += 1

        backtrack(0, [], left_remove, right_remove)

        return list(result)