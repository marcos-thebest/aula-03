p1 = int(input('Valor do primeiro produto: R$'))
p2 = int(input('Valor do segundo produto: R$'))
p3 = int(input('Valor do terceiro produto: R$'))
p4 = int(input('Valor do quarto produto: R$'))
p5 = int(input('Valor do quinto produto: R$'))

total = p1 + p2 + p3 + p4 + p5

print(f'O valor total da compra é: R${total}')

cliente = int(input('Qual o valor pago pelo cliente? R$ '))

troco = cliente - total

print(f'O valor do troco é: R${troco}')
