f = [[1, 5, 3], ['a', 'v', 3], ["sss", 'b'], [], [[3, 4, 5], ['a']], [(4, 5, 6), [4, 5, 6]]]


def fun1(all_list):
    return len(list(filter(lambda x: len([i for i in range(1, len(x)) if type(x[0]) is not type(x[i])]) > 0, all_list)))


print(fun1(f))

