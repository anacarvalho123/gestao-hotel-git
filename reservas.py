reservas = []

def criar_reserva(cliente, quarto):
    reservas.append((cliente, quarto))

def listar_reservas():
    for cliente, quarto in reservas:
        print(f"Cliente: {cliente} - Quarto: {quarto}")
