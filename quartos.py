quartos = {}

quartos = {
    101: "disponivel",
    102: "disponivel",
    103: "disponivel"
}

def listar_quartos():
    for numero, status in quartos.items():
        print(f"Quarto {numero} - {status}")
