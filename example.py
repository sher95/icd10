num = [3, 1, 4, 5, 2, 6, 7]


def even(func):
    res = 0
    for i in func:
        if i % 2 == 0:
            res = res + i
        else:
            print("odd numbers")
    print(res)


def test_even():
    even(num)