produtos = {}
produtos["bicicleta"] = {"Quantidade":12,"preço":1.50}
produtos["carro"] = {"Quantidade":25,"preço":1.40}
produtos["feijão"] = {"Quantidade":150,"preço":0.70}

for objeto,detalhes in produtos.items():
    print(f"Produto: {objeto} -- Quantidade: {detalhes['Quantidade']} -- Preço: {detalhes['preço']} ")