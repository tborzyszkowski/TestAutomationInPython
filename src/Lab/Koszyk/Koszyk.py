class Koszyk:
    def __init__(self) -> None:
        super().__init__()
        self.lista_produktow = []

    def add(self, produkt):
        self.lista_produktow.append(produkt)