reservas = []

def criar_reserva(cliente, quarto):
    reservas.append((cliente, quarto))

def listar_reservas():
    for cliente, quarto in reservas:
        print(f"Cliente: {cliente} - Quarto: {quarto}")

def cancelar_reserva(cliente):
    for reserva in reservas:
        if reserva[0] == cliente:
            reservas.remove(reserva)
            print("Reserva cancelada.")
            return
    print("Reserva nao encontrada.")
