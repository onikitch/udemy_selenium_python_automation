

def test_loop():
    hi = 4
    if hi > 5:
        print("matches")
        print("second line")
    else:
        print("do not match")
    print("code is completed")


def test_for():
    obj = [2, 3, 4, 6, 9]
    for i in obj:
        print(i*2)

def test_for_second():
    summation = 0
    for j in range(1, 7):
        summation = summation + j
    print(summation)