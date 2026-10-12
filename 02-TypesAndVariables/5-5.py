price_string = input("Enter price: ")
price_float = float(price_string)
discount_string = input("Enter discount %: ")
discount_int = int(discount_string)
price_with_discount = (100 - discount_int) / 100 * price_float
price_with_discount_float = round(price_with_discount,2)
reduction = discount_int / 100 * price_float
reduction_float = round(reduction,2)
print(f'Price with discount: {price_with_discount_float}')
print(f'Reduction: {reduction_float}')