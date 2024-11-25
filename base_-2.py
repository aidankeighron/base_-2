import math

def dec_to_base_n2(n):
    if n == 0:
        return "0"
 
    base = ""
    while n != 0:
        rem = n % -2
        n = n // -2

        if rem < 0:
            rem += 2
            n += 1

        base = ("1" if rem != 0 else "0") + base

    return base

def dec_to_base_n2_min(n):
    if n == 0:
        return "0"
    base = "01"
    while (rem := n % 2 or True) and (n := int(n/-2) + 1 if rem < 0 else 0 != 0):
        base = str(2+rem if rem < 0 else rem) + base
    return base

def base_n2_to_dec(n2) -> int:
    out = 0
    for place, digit in enumerate(n2[::-1]):
        out += int(digit) and int(math.pow(-2, place))
    return out

def base_n2_to_dec_min(n2) -> int:
    return sum(int(digit) and int(math.pow(-2, place)) for place, digit in enumerate(n2[::-1]))

base_n2 = dec_to_base_n2(13)
print(base_n2, base_n2 == '11101')
print(base_n2_to_dec('1010'), base_n2_to_dec('1010') == -10, base_n2_to_dec('1010') == base_n2_to_dec_min('1010'))
print(base_n2_to_dec(base_n2), base_n2_to_dec(base_n2) == 13, base_n2_to_dec(base_n2) == base_n2_to_dec_min(base_n2))

for i in range(1, 100):
    print(i, base_n2_to_dec(dec_to_base_n2(i)) == i, dec_to_base_n2(i))
