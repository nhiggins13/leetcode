from collections import defaultdict


class TwoSum:
    def __init__(self):
        self.nums = defaultdict(int)
        self.add_count = 0

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.add_count += 1
        self.nums[number] += 1

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        if self.add_count < 2:
            return False

        for num in self.nums:
            key = value - num
            if key in self.nums:
                if num == value - num:
                    if self.nums[key] > 1:
                        return True
                else:
                    return True

        return False


test = TwoSum()
test.add(3)
test.add(2)
test.add(1)
print(test.find(2))
