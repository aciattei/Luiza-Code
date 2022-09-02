#Criar função para adicionar item ao carrinho
#cart
cart = []

def add_item_cart(item, cart):
  #adicionar a lista intem à lista cart
  cart.append(item)
  return cart

def execute():
  id_user = input('Insira o id do usuário: ')
  id_product = input('Insira o id do produto: ')
  price_product = float(input('Insira o preço do produto: '))
  quantity_product = int(input('Insira a quantidade do produto: '))
  item = [id_user, id_product, price_product, quantity_product]
  cart = add_item_cart(item, cart)
  print(cart)

execute()