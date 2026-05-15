class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        minimizer=init

        for _ in range(iterations):
            derivation = 2 * minimizer
            minimizer = minimizer - derivation*learning_rate
        
        return round(minimizer,5)