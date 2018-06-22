# Changes a written number into an actual number.
# assumes no things like "thousand million" or "billion billion"
# commas and hyphens OK as long as there are spaces or hypnens between words

def num_word(num):
    """Convert word to number
        Ok with hyphens, commas, ands : as long as there are spaces or hyphens between all words
    """
    general_numbers = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
        "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11,
        "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15,
        "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19,
        "twenty": 20, "thirty": 30, "fourty": 40, "fifty": 50, "sixty": 60,
        "seventy": 70, "eighty": 80, "ninety": 90
        }

    multiplier_numbers = {"hundred": 100, "thousand": 1000, "million": 1000000,
    "billion": 1000000000, "trillion":10000000000
    }

    # turn the string into a list of individual words

    num = num.split()
    for i in range(len(num)):
        if "-" in num[i]:
            both_numbers = num[i].split("-")
            num[i] = both_numbers[0]
            num.insert(i+1, both_numbers[1])

    # remove any commas
    for d in range(len(num)):
        if num[d][-1] == ",":
            num[d] = num[d][0:-1]
    
    # answer starts at 0, and decimal status starts at no
    answer = 0
    is_decimal = "no"

    # Tests for a decimal
    if "point" in num:
        is_decimal = "yes"
        decimal = num.index("point")
        after_decimal = num[decimal+1:]
        num = num[:decimal]

    #find the current multiplier
    def current_multiplier(place, num_list):
        # if it's not in the last place
        if place < (len(num_list) - 1):
            #print("{} not in last index".format(num[place]))
            # check every position after for a multiplier
            for x in range(place + 1, len(num_list)):
                #print("checking for multipliers after {}".format(num[place]))
                # if there is a multiplier
                if num_list[x] in multiplier_numbers:
                    #print("multiplier found")
                    # check for special case of "hundred" as that can combo with other multipliers
                    if num_list[x] == "hundred" and place < len(num_list) - 2:
                        #print("multiplier = hundred")
                        # see if there is a second multiplier
                        for j in range(x + 1, len(num_list)):
                            #print("looking for second multiplier")
                            
                            if num[j] in multiplier_numbers:
                                #if there is a second multiplier, return 100 * second multiplier
                                return 100 * multiplier_numbers[num_list[j]]
                        else:
                            # there was no second multiplier to combo with, so return 100
                            return 100

                    else:
                        #the multiplier wasn't "hundred" so it couldn't combo with another multiplier
                        return multiplier_numbers[num_list[x]]
            else:
                #no multiplier found
                return 1
        else:
            #it's in last position, no multiplier possible
            return 1

    for c in range(len(num)):
        if num[c] in general_numbers:
            current_number = general_numbers[num[c]] * current_multiplier(c, num)
            answer += current_number
    
    if is_decimal == "yes":
        for g in range(len(after_decimal)):
            decimal_multiplier = 1/ 10**(g+1)
            current_number = decimal_multiplier * general_numbers[after_decimal[g]]
            answer += current_number

    if num[0] == "negative":
        answer *= -1

    return answer


a = "negative four million, five hundred and sixty-three thousand point three two five"

print (num_word(a))
