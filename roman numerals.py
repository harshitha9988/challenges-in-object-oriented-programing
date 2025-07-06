class RomanConverter:
    def __init__(self):
        # Define Roman numeral symbols and their corresponding integer values
        self.value_map = [
            (1000, 'M'),
            (900,  'CM'),
            (500,  'D'),
            (400,  'CD'),
            (100,  'C'),
            (90,   'XC'),
            (50,   'L'),
            (40,   'XL'),
            (10,   'X'),
            (9,    'IX'),
            (5,    'V'),
            (4,    'IV'),
            (1,    'I')
        ]

    def int_to_roman(self, num):
        if not (1 <= num <= 3999):
            raise ValueError("Number out of range (must be between 1 and 3999)")
        result = ''
        for value, symbol in self.value_map:
            while num >= value:
                result += symbol
                num -= value
        return result

if __name__ == "__main__":
    converter = RomanConverter()
    number = int(input("Enter an integer (1–3999): "))
    roman_numeral = converter.int_to_roman(number)
    print(f"Roman numeral: {roman_numeral}")