from Koszyk import Koszyk, NoProduktInKoszykException, EmptyKoszykException
from Produkt import Produkt

if __name__ == '__main__':
    koszyk = Koszyk()
    print(koszyk)
    aaa = "" + str(koszyk)
    print(aaa)
    l = [koszyk]
    print(str(l))
    try:
        koszyk.remove(Produkt())
    except NoProduktInKoszykException:
        print("NoProduktInKoszykException")
    except EmptyKoszykException:
        print("EmptyKoszykException")
