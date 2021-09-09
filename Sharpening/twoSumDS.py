class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.integers = []
        

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.integers = self.integers + [number]
        

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """

        n = len(self.integers)
        for i in range(n):
            for j in range(i, n):
                if i==j:
                    continue
                sum_ij = self.integers[i] + self.integers[j]
                if value == sum_ij:
                    return True
        return False