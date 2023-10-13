from Koszyk import Koszyk, NoProduktInKoszykException, EmptyKoszykException
from Produkt import Produkt

if __name__ == '__main__':
    koszyk = Koszyk()
    try:
        koszyk.remove(Produkt())
    except NoProduktInKoszykException:
        print("NoProduktInKoszykException")
    except EmptyKoszykException:
        print("EmptyKoszykException")
