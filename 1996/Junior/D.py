def roman_to_int(roman):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    prev_value = 0

    for i in reversed(roman):
        if roman_dict[i] >= prev_value:
            num += roman_dict[i]
        else:
            num -= roman_dict[i]
        prev_value = roman_dict[i]

    return num


def int_to_roman(num):
    if num >= 1000:
        return "CONCORDIA CUM VERITATE"

    roman_numerals = [
        ("M", 1000), ("CM", 900), ("D", 500), ("CD", 400),
        ("C", 100), ("XC", 90), ("L", 50), ("XL", 40),
        ("X", 10), ("IX", 9), ("V", 5), ("IV", 4), ("I", 1)
    ]

    roman = ""
    for symbol, value in roman_numerals:
        while num >= value:
            roman += symbol
            num -= value

    return roman


def roman_calculator(input_lines):
    results = []
    for line in input_lines:
        operands = line.split('+')
        operand1, operand2 = operands[0], operands[1][:-1] 

        sum_int = roman_to_int(operand1) + roman_to_int(operand2)
        sum_roman = int_to_roman(sum_int)

        results.append(f"{operand1}+{operand2}={sum_roman}")

    return results

sample_input = ["VII+II=", "XXIX+X=", "M+I="]
roman_calculator(sample_input)
