from math import ceil


def num_to_word(num):
    """Convert number to a word."""
    general_numbers = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
        6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 
        12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 
        16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 
        20: 'twenty', 30: 'thirty', 40: 'fourty', 50: 'fifty', 60: 'sixty', 
        70: 'seventy', 80: 'eighty', 90: 'ninety'
        }

    multiplier_numbers = {1000: "thousand,", 1000000: "million,", 1000000000: "billion,",
        1000000000000: "trillion,"
        }
    multiplier_list = ["thousand,", "million,", "billion", "trillion"]

    answer = []

    if num == 0:
        return "zero"
    if num < 0:
        answer.append("negative")

    # if there are decimal points, we're gonna turn that into a string because
    # it does not work right math-wise
    decimal = []
    decimal.extend(str(num))
    if "." in decimal:
        decimal = decimal[(str(num).find(".")):]

    print(decimal)
    num = int(num)

    multiplier = 1
    while num / multiplier >= 1000:
        multiplier *= 1000

    while num > 0:
        # working with a max of 3 digits
        current_num = num // multiplier
        # removing those 3 digits from left side of number
        num -= (current_num * multiplier)
        if current_num >= 100:
            hund = current_num // 100
            answer.extend([general_numbers[hund], "hundred"])
            current_num -= (hund * 100)
            if current_num > 0:
                answer.append("and")
        if current_num >= 20:
            ones = current_num % 10
            current_num -= ones
            if ones:
                answer.append(f"""{general_numbers[current_num]}-
                    {general_numbers[ones]}""")
            else:
                answer.append(general_numbers[current_num])
            current_num = 0
        else:
            answer.append(general_numbers[current_num])
            current_num = 0
        if multiplier in multiplier_numbers:
            answer.append(multiplier_numbers[multiplier])
        multiplier /= 1000
        
    if answer[-1] in multiplier_list:
        answer[-1] = answer[-1].rstrip(",")

    if decimal:
        answer.append("point")

        for num in decimal[1:]:
            answer.append(general_numbers[int(num)])

    answer = " ".join(answer)

    return answer




print(num_to_word(8172831000.14))





