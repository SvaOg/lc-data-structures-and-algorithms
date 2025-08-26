def get_digit_sum(num):
    sum = 0
    while num:
        digit = num % 10
        sum += digit
        num //= 10
    return sum


def test_001():
    assert get_digit_sum(11) == 2
    assert get_digit_sum(12345) == 15
