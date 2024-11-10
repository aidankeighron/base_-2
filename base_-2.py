import math

# def dec_to_base_n2(n):
#     base_2 = ""
#     print(bin(n)[2:])
#     while n >= 1:
#         base_2 += str(n&1)
#         n >>= 1
#     print(base_2[::-1])

def dec_to_base_n2(n):
    for i in range(n):
        print(i, int(math.pow(-2, i)))

def base_n2_to_dec(n2) -> int:
    out = 0
    for place, digit in enumerate(n2[::-1]):
        out += int(digit) and int(math.pow(-2, place))
    print(out)
    return out


# 16 -8 4 -2 1
dec_to_base_n2(8)
base_n2_to_dec('000')
base_n2_to_dec('001')
base_n2_to_dec('010')
base_n2_to_dec('011')
base_n2_to_dec('100')
base_n2_to_dec('101')
base_n2_to_dec('110')
base_n2_to_dec('111')
# dec_to_base_n2(2)
# dec_to_base_n2(3)
