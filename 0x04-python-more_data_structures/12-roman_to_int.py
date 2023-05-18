#!/usr/bin/python3
class Solution:
    def roman_to_int(self, roman_string):
        if not isinstance(roman_string, str) or roman_string is None:
            return 0
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        number = 0
        for i in range(len(roman_string)):
            if i < len(roman_string) - 1:
                if roman[roman_string[i]] < roman[roman_string[i + 1]]:
                    number -= roman[roman_string[i]]
                else:
                    number += roman[roman_string[i]]
        number += roman[roman_string[-1]]  # Add the last roman numeral
        return number


# task = Solution()
# print(task.roman_to_int('MCMXCIV'))  # Output: 1994
