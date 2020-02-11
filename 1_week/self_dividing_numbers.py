class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        return [i for i in range(left, right + 1) if all(int(n) and not i % int(n) for n in str(i))]
