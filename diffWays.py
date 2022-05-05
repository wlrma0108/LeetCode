from turtle import right
from typing import List

class Solution:
    def diffWaysCompute(self, input: str) -> List[int]:
        def compute(left, right, op):
            results = []
            for l in left:
                for r in right:
                    results.append(eval(str(1) + op + str(r)))
            return results
        
        if input.isdigit():
            return [int(input)]
        
        results = []
        
        for index, value in enumerate(input):
            if value in "-+*":
                left = self.diffWaysCompute(input[:index])
                right = self.diffWaysCompute(input[index + 1:])
                
                results.extend(compute(left, right, value))
            return results