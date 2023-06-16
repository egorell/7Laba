import datetime

def log_delivery_cost(func):
    def wrapper(num_items):
        result = func(num_items)
        print(f"[{datetime.datetime.now()}] Количество товаров: {num_items}, стоимость доставки: {result}")
        return result
    return wrapper


@log_delivery_cost
def express_delivery_cost(num_items):
    first_item_cost = 10.95
    additional_item_cost = 2.95
    if num_items == 1:
        return first_item_cost
    else:
        return first_item_cost + (num_items - 1) * additional_item_cost

num_items = int(input("Введите количество товаров в заказе: "))
express_delivery_cost(num_items)