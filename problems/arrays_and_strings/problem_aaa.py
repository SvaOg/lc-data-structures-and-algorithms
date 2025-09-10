def find_length(nums, k):
    # curr is the current sum of the window
    left = curr = ans = 0
    for right in range(len(nums)):
        curr += nums[right]
        while curr > k:
            curr -= nums[left]
            left += 1
        ans = max(ans, right - left + 1)

    return ans


def binary_string(s):
    left = curr = ans = 0
    for right in range(len(s)):
        if s[right] == "0":
            curr += 1
        while curr > 1:
            if s[left] == "0":
                curr -= 1
            left += 1
        ans = max(ans, right - left + 1)

    return ans


def test_001():
    assert find_length([2, 2, 2], 1) == 0


def test_002():
    assert binary_string("00000000000") == 1


def test_003():
    assert binary_string("10000000000") == 2


def answer_queries(nums, queries, limit):
    prefix = [nums[0]]
    for n in range(1, len(nums)):
        prefix.append(nums[n] + prefix[-1])

    answer = []
    for x, y in queries:
        sum = prefix[y] - prefix[x] + nums[x]
        answer.append(sum < limit)

    return answer


def test_004():
    nums = [1, 6, 3, 2, 7, 2]
    queries = [[0, 3], [2, 5], [2, 4]]
    limit = 13
    expected = [True, False, True]

    assert answer_queries(nums, queries, limit) == expected
