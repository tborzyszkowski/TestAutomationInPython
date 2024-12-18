class EmptyKoszykException(Exception):
    pass

class NoProduktInKoszykException(Exception):
    pass

class Koszyk:
    def __init__(self, lista_produktow = None) -> None:
        super().__init__()
        self.lista_produktow = lista_produktow if lista_produktow else []

    def add(self, produkt):
        self.lista_produktow.append(produkt)

    def remove(self, produkt):
        if self.lista_produktow:
            if produkt in self.lista_produktow:
                self.lista_produktow.remove(produkt)
            else:
                raise NoProduktInKoszykException()
        else:
            raise EmptyKoszykException()

    def __repr__(self):
        return "Repr"

    def __str__(self):
        return "Str"