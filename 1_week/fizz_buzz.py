class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        results = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                results.append('FizzBuzz')
            elif i % 3 == 0:
                results.append('Fizz')
            elif i % 5 == 0:
                results.append('Buzz')
            else:
                results.append(str(i))
        return results
        # return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n + 1)]
