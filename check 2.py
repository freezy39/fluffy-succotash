from datetime import datetime

def convert_to_words(number):
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", 
             "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", 
            "sixty", "seventy", "eighty", "ninety"]

    def one_to_99(n):
        if n < 10:
            return ones[n]
        elif n < 20:
            return teens[n - 10]
        else:
            return tens[n // 10] + (" " + ones[n % 10] if n % 10 != 0 else "")

    def one_to_999(n):
        if n < 100:
            return one_to_99(n)
        else:
            return ones[n // 100] + " hundred" + (
                " " + one_to_99(n % 100) if n % 100 != 0 else ""
            )

    def group(n, name):
        return "" if n == 0 else one_to_999(n) + " " + name

    if number == 0:
        return "zero dollars"

    parts = []
    billions = number // 1_000_000_000
    millions = (number // 1_000_000) % 1000
    thousands = (number // 1_000) % 1000
    remainder = number % 1000

    if billions:
        parts.append(group(billions, "billion"))
    if millions:
        parts.append(group(millions, "million"))
    if thousands:
        parts.append(group(thousands, "thousand"))
    if remainder:
        parts.append(one_to_999(remainder))

    return " ".join(parts) + " dollars"

# Test examples
examples = [0, 5, 13, 27, 105, 999, 1001, 10521, 1000000, 302450789]
for amount in examples:
    print(f"${amount} -> {convert_to_words(amount)}")
