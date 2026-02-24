clientes = []

def registar_cliente(nome):
    clientes.append(nome)

def listar_clientes():
    for cliente in clientes:
        print(cliente)