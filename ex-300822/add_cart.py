cart = []

id_user = input('Insira o id do usuário: ')
id_product = input('Insira o id do produto: ')
price_product = float(input('Insira o preço do produto: '))
quantity_product = int(input('Insira a quantidade do produto: '))

item = [id_user, id_product, price_product, quantity_product]
#id_user, id_product, price_product, quantity_product
def add_item_cart():
  cart.append(item)
  return cart
  
def get_all_items_cart():
  return cart

def get_item_cart_by_id(id_product):
  new_list = [item for item in cart if item[0 == id_product]]
  return new_list

  #remove
  #usar pop
  
  #calcular o total do carrinho