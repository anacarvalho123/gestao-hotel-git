from clientes import registar_cliente, listar_clientes
from quartos import listar_quartos, ocupar_quarto, liberar_quarto
from reservas import criar_reserva, listar_reservas, cancelar_reserva

print("=== Sistema de Gestao de Hotel ===")

# Teste clientes
registar_cliente("Ana")
registar_cliente("Carlos")
print("\nClientes registados:")
listar_clientes()

# Teste quartos
print("\nQuartos disponiveis:")
listar_quartos()

ocupar_quarto(101)

print("\nQuartos apos ocupar 101:")
listar_quartos()

# Teste reservas
criar_reserva("Ana", 101)
print("\nReservas atuais:")
listar_reservas()

cancelar_reserva("Ana")
print("\nReservas apos cancelamento:")
listar_reservas()
