import cart

qnt_items = int(input('Quantos itens deseja comprar: '))
id_user = input('Insira o id do usuário: ')

count = 0
while count < qnt_items:
    id_product = input('Insira o id do produto: ')
    price_product = float(input('Insira o preço do produto: '))
    quantity_product = int(input('Insira a quantidade do produto: '))
    cart.add_item_cart(id_user, id_product, price_product, quantity_product)
    count += 1