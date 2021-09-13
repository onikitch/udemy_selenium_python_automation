

def test_list():

    values = [0, 1, 2, 3, 4, 5] # 0, 1, 2, 3, 4, 5
    print(values)

    values.insert(3, "super") # 0, 1, 2, 'super', 3, 4, 5
    print(values)

    values.append("end") # 0, 1, 2, 'super', 3, 4, 5, 'end'
    print(values)

    values[2] = "update" # 0, 1, 'update', 'super', 3, 4, 5, 'end'
    print(values)

    del values[0] # 1, 'update', 'super', 3, 4, 5, 'end'
    print(values)

