class Produto:
    def __init__(self, nome, preco, quantidade, estoque):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.valor_total = preco * quantidade
        self.estoque = estoque - quantidade
    
def inserir_produto():
    nome = input("Insira o nome do produto: ")
    quantidade = int(input("Informe a quantidade do produto: "))
    preco = float(input("Informe o preço do produto: "))
    estoque = int(input("Informe a quantidade em estoque: "))



