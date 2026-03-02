# api/numbers.py

class NaturalNumbersSet:
    def __init__(self):
        self.original_set = list(range(1, 101))
        self.current_set = self.original_set.copy()
        self.extracted_number = None

    def extract(self, number: int):
        if not isinstance(number, int):
            raise ValueError("El número debe ser entero")

        if number < 1 or number > 100:
            raise ValueError("El número debe estar entre 1 y 100")

        if number not in self.current_set:
            raise ValueError("El número ya fue extraído")

        self.current_set.remove(number)
        self.extracted_number = number

    def find_missing(self):
        expected_sum = sum(self.original_set)
        current_sum = sum(self.current_set)
        return expected_sum - current_sum