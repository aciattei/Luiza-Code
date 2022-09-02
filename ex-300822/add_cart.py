cart = []
cart_total = 0

def add_cart(item_id, item_price):
  cart.append(item_id)
  return item_price
cart_total += add_cart('Apple', 100)

print(cart)
print(cart_total)