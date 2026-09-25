class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:

        def parse(i):
            parts = []
            current = {""}

            while i < len(expression) and expression[i] != '}':
                
                if expression[i] == ',':
                    parts.append(current)
                    current = {""}
                    i += 1

                elif expression[i] == '{':
                    inside, i = parse(i + 1)

                    current = {
                        a + b
                        for a in current
                        for b in inside
                    }

                else:
                    # Letter
                    current = {
                        word + expression[i]
                        for word in current
                    }
                    i += 1

            parts.append(current)

            # Union everything separated by commas
            result = set()
            for part in parts:
                result |= part

            if i < len(expression) and expression[i] == '}':
                i += 1

            return result, i

        # Parse the whole expression
        ans, _ = parse(0)

        return sorted(ans)