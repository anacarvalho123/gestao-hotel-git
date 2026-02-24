clientes = []

def registar_cliente(nome):
    clientes.append(nome)

def listar_clientes():
    if not clientes:
        print("Nenhum cliente registado.")
    else:
        for cliente in clientes:
            print(cliente)
