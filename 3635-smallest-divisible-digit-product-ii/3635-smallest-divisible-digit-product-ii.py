def get_prime_factors(t):
    c2 = c3 = c5 = c7 = 0
    while t % 2 == 0:
        c2 += 1
        t //= 2
    while t % 3 == 0:
        c3 += 1
        t //= 3
    while t % 5 == 0:
        c5 += 1
        t //= 5
    while t % 7 == 0:
        c7 += 1
        t //= 7
    if t > 1:
        return -1
    return (c2, c3, c5, c7)


def min_digits_needed(c2, c3, c5, c7):
    c2, c3, c5, c7 = max(0, c2), max(0, c3), max(0, c5), max(0, c7)
    digits = []
    tem = 0

    if c5 > 0:
        tem += c5
        digits.extend([5] * c5)
        c5 = 0
    if c7 > 0:
        tem += c7
        digits.extend([7] * c7)
        c7 = 0
    if c3 >= 2:
        tem += c3 // 2
        digits.extend([9] * (c3 // 2))
        c3 %= 2
    if c2 >= 3:
        tem += c2 // 3
        digits.extend([8] * (c2 // 3))
        c2 %= 3
    if c3 == 1 and c2 == 1:
        tem += 1
        digits.append(6)
        c3 = c2 = 0
    if c3 == 1 and c2 == 2:
        tem += 2
        digits.extend([2, 6])
        c3 = c2 = 0
    if c3 == 1:
        tem += 1
        digits.append(3)
        c3 = 0
    if c2 == 2:
        digits.append(4)
        tem += 1
        c2 = 0
    if c2 == 1:
        digits.append(2)
        tem += 1
        c2 = 0

    digits.sort()
    return tem, digits


def get_digit_factors(cur):
    c2 = c3 = c5 = c7 = 0
    if cur == 9:
        c3 = 2
    elif cur == 8:
        c2 = 3
    elif cur == 7:
        c7 = 1
    elif cur == 6:
        c2 = 1
        c3 = 1
    elif cur == 5:
        c5 = 1
    elif cur == 4:
        c2 = 2
    elif cur == 3:
        c3 = 1
    elif cur == 2:
        c2 = 1
    return c2, c3, c5, c7


def solve(num, t):
    num = str(num)
    factors = get_prime_factors(t)
    if factors == -1:
        return "-1"
    orig_c2, orig_c3, orig_c5, orig_c7 = factors

    full_c2 = full_c3 = full_c5 = full_c7 = 0
    zero_count = 0
    for char in num:
        if char == "0":
            zero_count += 1
        else:
            fc2, fc3, fc5, fc7 = get_digit_factors(int(char))
            full_c2 += fc2
            full_c3 += fc3
            full_c5 += fc5
            full_c7 += fc7

    if zero_count == 0 and (
        full_c2 >= orig_c2
        and full_c3 >= orig_c3
        and full_c5 >= orig_c5
        and full_c7 >= orig_c7
    ):
        return num

    p_c2, p_c3, p_c5, p_c7 = full_c2, full_c3, full_c5, full_c7

    for i in range(len(num) - 1, -1, -1):
        cur_char = num[i]

        if cur_char == "0":
            zero_count -= 1
        else:
            fc2, fc3, fc5, fc7 = get_digit_factors(int(cur_char))
            p_c2 -= fc2
            p_c3 -= fc3
            p_c5 -= fc5
            p_c7 -= fc7

        if zero_count > 0:
            continue

        prefix = num[:i]
        start_d = int(cur_char) + 1

        for d in range(start_d, 10):
            d_c2, d_c3, d_c5, d_c7 = get_digit_factors(d)

            rem_c2 = orig_c2 - (p_c2 + d_c2)
            rem_c3 = orig_c3 - (p_c3 + d_c3)
            rem_c5 = orig_c5 - (p_c5 + d_c5)
            rem_c7 = orig_c7 - (p_c7 + d_c7)

            tem, digits = min_digits_needed(rem_c2, rem_c3, rem_c5, rem_c7)
            spaces_left = len(num) - 1 - i

            if spaces_left >= tem:
                digits.sort()
                suffix_str = "".join(map(str, digits))
                ones_needed = spaces_left - tem
                padding_ones = "1" * ones_needed
                return prefix + str(d) + padding_ones + suffix_str

    tem, digits = min_digits_needed(orig_c2, orig_c3, orig_c5, orig_c7)
    digits.sort()
    suffix_str = "".join(map(str, digits))

    new_length = max(len(num) + 1, tem)
    ones_needed = new_length - tem
    padding_ones = "1" * ones_needed
    return padding_ones + suffix_str


class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        return solve(num, t)
