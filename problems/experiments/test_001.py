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


def test_002():
    a = [1, 2, 3]
    a.append(4)
    assert a == [1, 2, 3, 4]
