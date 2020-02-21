from collections import Counter
import re


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        parse = re.findall(r'([A-Z][a-z]*)(\d*)|(\()|(\))(\d*)', formula)
        stack = [Counter()]
        for name, count, left_paren, right_paren, mult in parse:
            if name:
                stack[-1][name] += int(count or 1)
            if left_paren:
                stack.append(Counter())
            if right_paren:
                apex = stack.pop()
                for key in apex:
                    stack[-1][key] += apex[key] * int(mult or 1)

        return ''.join((name + str(stack[-1][name]) if stack[-1][name] > 1 else name)
                       for name in sorted(stack[-1]))
