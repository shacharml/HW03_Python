Dough = {'Thick': 40, 'Thin': 30, 'Gluten_Free_Thick': 20, 'Gluten_Free_Soft': 10}
Sauce = {'Tomatoes': 30, 'Rosa': 40, 'Pesto': 50, 'Spinach_With_Cream': 60}
Cheese = {'Parmesan': 100, 'Mozzarella': 90, 'vegan': 60}
Extras = {'Olives': 30, 'Corn': 15, 'Tomatoes': 10, 'Onion': 20}


class Decorator:

    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        result = self.function(*args, **kwargs)

        return result


@Decorator
def get_sum(*args, **kwargs):
    total_cal = 0
    pizza = args[0]
    for p in pizza:
        if Cheese.__contains__(p):
            ch = p
        elif p == 'double':
            if pizza[p] == 2:
                total_cal += 2 * pizza[ch]
            if pizza[p] == 1:
                total_cal += pizza[ch]
        else:
            total_cal += pizza[p]

    return total_cal


# double: without cheese:0,Regular:1,double:2
pizza = {'Thin': Dough['Thin'], 'Parmesan': Cheese['Parmesan'], 'Tomatoes': Sauce['Tomatoes'],
         'Olives': Extras['Olives'], 'double': 1}
deco = Decorator(get_sum)

print(deco(pizza))
