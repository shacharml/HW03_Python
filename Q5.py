
d = {'All_call_f': 0, 'All_param': 0}
type1 = {}


def decorator(original_func):  # the outer function that gets a function as parameter
    func_name = original_func

    current_f = 0

    def wrapper(*args, **kwargs):  # inner function that uses the original function but wraps it
        global d
        nonlocal current_f
        d['All_call_f'] += 1
        if func_name == original_func:
            current_f += 1
            d['All_param'] += len(args) + len(kwargs)
        else:
            current_f = 1

        print("functional name ", func_name.__name__, " calls:")
        print("Total number of calls to decorated functions : ", d["All_call_f"])
        print("Total number of calls to current function : ", current_f)
        print("Total number of arguments : ", d["All_param"], "\n")

        v = original_func(*args, **kwargs)
        type_V = type(v)
        if type1.keys().__contains__(type_V):
            type1[type_V] += 1
        else:
            type1[type_V] = 1
        for t in type1:
            print("Type ", t.__name__, " , used : ", type1.get(t))

    return wrapper


@decorator
def do1(*args, **kwargs):
    return args


@decorator
def do2(*args, **kwargs):
    return 'our func'


do1(1, 2, 3)
do1('s')
do1()
do2('add')
do2()
