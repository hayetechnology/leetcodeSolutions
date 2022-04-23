mappings = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26,
}
mappings_inv = {v: k for k, v in mappings.items()}


def rec_funct(num):
    num_of_digits = len(str(num))
    ways = 0
    if num_of_digits > 2:
        fst_digit = int(num / pow(10, num_of_digits - 1))
        sec_digit = int(num / pow(10, num_of_digits - 2) % 10)
        rest1 = num - int(num / pow(10, num_of_digits - 1)) * pow(10, num_of_digits - 1)
        if 0 < fst_digit < 10:
            ways = ways + rec_funct(rest1)
            val = (fst_digit * 10) + sec_digit
            if 0 < val < 27:
                rest2 = num - int(num / pow(10, num_of_digits - 2)) * pow(10, num_of_digits - 2)
                ways = ways + rec_funct(rest2)
            return ways
        else:
            return -1000
    elif num_of_digits == 2:
        fst_digit = int(num / pow(10, num_of_digits - 1))
        sec_digit = int(num / pow(10, num_of_digits - 2) % 10)
        rest1 = num - int(num / pow(10, num_of_digits - 1)) * pow(10, num_of_digits - 1)
        if 0 < fst_digit < 10:
            ways = ways + rec_funct(rest1)
            val = (fst_digit * 10) + sec_digit
            if 0 < val < 27:
                return ways + 1
            return ways
        else:
            return -1000
    else:
        if 0 < num < 10:
            return 1


print(rec_funct(22))
