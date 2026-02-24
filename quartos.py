quartos = {}

quartos = {
    101: "disponivel",
    102: "disponivel",
    103: "disponivel"
}

def listar_quartos():
    for numero, status in quartos.items():
        print(f"Quarto {numero} - {status}")

def ocupar_quarto(numero):
    if numero in quartos:
        quartos[numero] = "ocupado"
        print(f"Quarto {numero} agora esta ocupado.")
    else:
        print("Quarto nao existe.")

def liberar_quarto(numero):
    if numero in quartos:
        quartos[numero] = "disponivel"
        print(f"Quarto {numero} agora esta disponivel.")
    else:
        print("Quarto nao existe.")
