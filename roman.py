ROMANS = {
        'M' : 1000,
        'D' : 500,
        'C' : 100,
        'L' : 50,
        'X' : 10,
        'V' : 5,
        'I' : 1
    }


class NotInListException(Exception):
    pass


def dec_to_roman(num):
    try:
        rom = []
        for k, v in ROMANS.items():
            div = num // v
            if div:
                rom.append(k * div)
            num -= div * v
            if v - (num - num % 100) == 100 and (k == 'M' or k == 'D'):
                rom.append('C')
                rom.append(k)
                num -= v - 100
            elif v - (num - num % 10) == 10 and (k == 'C' or k == 'L'):
                rom.append('X')
                rom.append(k)
                num -= v - 10
            elif v - num == 1 and (k == 'X' or k == 'V'):
                rom.append('I')
                rom.append(k)
                num -= v - 1
        return "".join(rom)
    except:
        return "The input is not a valid decimal number."


def roman_to_dec(rom):
    try:
        roman_chars = list(ROMANS)
        num = 0
        for i, c in enumerate(rom):
            if c not in ROMANS or i < len(rom) - 1 and rom[i+1] not in ROMANS:
                raise ValueError(f"{rom} is not a valid Roman number.")
            if i < (len(rom) - 1) and roman_chars.index(c) > roman_chars.index(rom[i+1]):
                print(roman_chars.index(c), roman_chars.index(rom[i+1]))
                num -= ROMANS[c]
            else:
                num += ROMANS[c]
        if rom != dec_to_roman(num):
            raise ValueError(f"{rom} is not a valid Roman number.")
        return num
    except ValueError as e:
        return f"ValueError: {e}"
    except Exception as e:
       print(f"An unexpected error occurred: {e}")


def main():
    print(roman_to_dec('XXMM'))
    print("-" * 10)
    print(dec_to_roman(13))


main()