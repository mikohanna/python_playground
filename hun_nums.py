def dec_to_hun(num):
    if num == 0:
        return "nulla"
    szamok = {
        0: ('', ''),
        1: ('egy', 'tizen', 'tíz'),
        2: ('két', 'huszon', 'húsz'),
        3: ('három', 'harminc'),
        4: ('négy', 'negyven'),
        5: ('öt', 'ötven'),
        6: ('hat', 'hatvan'),
        7: ('hét', 'hetven'),
        8: ('nyolc', 'nyolcvan'),
        9: ('kilenc', 'kilencven')
    }
    num_str = str(num)[::-1]
    groups = [num_str[i:i+3] for i in range(0, len(num_str), 3)]  # Hármas csoportok
    number_groups = [int(group[::-1]) for group in groups] 
    print(number_groups)
    hun_groups = ["", "ezer", "millió", "milliárd"]
    hun_num = ""
    for i, group in enumerate(number_groups):
        if group == 0:
            continue
        group_str = ""
        for j, digit in enumerate(str(group)[::-1]):
            digit = int(digit)
            if j == 0:
                group_str = szamok[digit][0] + group_str
            elif j == 1:
                if digit == 1 and len(str(group)) > 2:
                    group_str = szamok[digit][2] + group_str
                else:
                    group_str = szamok[digit][1] + group_str
            elif j == 2:
                group_str = szamok[digit][0] + "száz" + group_str
        hun_num = group_str + hun_groups[i] + "-" + hun_num
    hun_num = hun_num.rstrip("-")
    if hun_num.endswith("két"):
        hun_num = hun_num[:-3] + "kettő"
    return hun_num


print(dec_to_hun(1000002122))