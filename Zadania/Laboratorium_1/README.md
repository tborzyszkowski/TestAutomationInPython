**Zadanie 1**

Napisz program, który będzie realizował grę pod tytułem **FizzBuzz**. Reguły tej gry są następujące:

* Pobieramy liczbę całkowitą od użytkownika
* Jeżeli liczba ta jest podzielna przez 15 wypisujemy na ekran "FizzBuzz" (wraz z cudzysłowiami)
* W przeciwnym przypadku jeżeli liczba ta jest podzielna przez 3 wypisujemy na ekran "Fizz" (wraz z cudzysłowami)
* W przeciwnym przypadku jeżeli liczba ta jest podzielna przez 5 wypisujemy na ekran "Buzz" (wraz z cudzysłowiami)
* W przeciwnym przypadku wypisujemy tę liczbę z cudzysłowiami np: "17"

**Wskazówka:** Aby wykonać to zadanie należy pamiętać, że liczbę należy zamienić na typ string. Służy do tego funkcja str(napis).

``Sample Input:
3``

``Sample Output:
"Fizz"``

***

**Zadanie 2**

Napisz program, który pobierze dwie liczby całkowite a,b większe od zera i wyświetli następujący prostokąt o długości a i szerokości b.

Nie zakładamy tutaj błędnych danych wyjściowych.

**Znak | ma reprezentować w programie znak spacji**.

`Sample Input 1:
3
3`

`Sample Output 1:`

`***`  
`*|*`  
`***`  

`Sample Input 2: 5 5`

`Sample Output 2:`

`*****`  
`*|||*`  
`*|||*`  
`*|||*`  
`*****`  

***

**Zadanie 3** 

Napisz funkcję **is_pangram(word)**, który sprawdza czy dany ciąg tekstowy jest pangramem.

Pangramem nazywamy ciąg tekstowy, w którym każda litera alfabetu łacińskiego występuje co najmniej raz.

W przypadku pozytywnej odpowiedzi funkcja powinna zwracać **True**, w przeciwnym przypadku **False**.

**Przykładowo**:

`is_pangram('') == False`
`is_pangram('abcdefghijklmnopqrstuvwxyz') == True`

***

**Zadanie 4**

Napisz funkcję **is_key(dictionary, key)**, który zwraca wartość **True**, jeżeli w słowniku dictionary znajduje się klucz key, a **False** w przeciwnym przypadku.

**Napisz wyłącznie funkcję**.

***

**Zadanie 5**

W systemie znajduje się plik **data.csv**, który wygląda następująco:

`department_id,department_name,manager_id,location_id
10,Administration,200,1700
20,Marketing,201,1800
30,Purchasing,114,1700
40,Human Resources,203,2400
50,Shipping,121,1500`

Napisz program, który wyświetli linie nie zawierające pola manager_id oraz bez nagłówka.

***

**Zadanie 6**

Napisz program, który pobierze od użytkownika liczbę całkowitą n, a następnie w pliku words.txt umieści wszystkie litery z alfabetu łacińskiego tak że w jednej linii będzie nn znaków dużymi literami. 

W przypadku kiedy liter zabraknie, to zostawiamy je nie dopełniając je żadnymi znakami.

Nie wypisuj funkcji, która wypisuje zawartość pliku words.txt

`Sample Input:
3`

`Sample Output:
ABC
DEF
GHI
JKL
MNO
PQR
STU
VWX
YZ`

***

**Zadanie 7**

Jeżeli podamy wiek w sekundach, to jest możliwość obliczenia ile osoba ta ma lat na ziemi.

Kula ziemska przechodzi przez własną orbitę przez 365,25 dnia, które wynosi równo 31557600 sekund.

A więc jeżeli osoba ma 1000000000 sekund to łatwo można policzyć, że 1000000000/31557600 = 31,69 lat (w przybliżeniu do drugiego miejsca po przecinku).

Teraz rozpatrzmy metodę, która będzie przyjmowała wiek w sekundach oraz planetę którą chcemy obliczyć.

Napisz program, który będzie zawierał tę metodę uwzględniając poniższe dane dotyczące innych planet:

* Obrót Merkurego podczas własnej orbity wynosi 0.2408467 lat ziemskich
* Obrót Wenus podczas własnej orbity wynosi 0.61519726 lat ziemskich
* Obrót Marsa podczas własnej orbity wynosi 1.8808158 lat ziemskich
* Obrót Jowisza podczas własnej orbity wynosi 11.862615 lat ziemskich
* Obrót Saturna podczas własnej orbity wynosi 29.447498 lat ziemskich
* Obrót Uranu podczas własnej orbity wynosi 84.016846 lat ziemskich
* Obrót Neptuna podczas własnej orbity wynosi 164.79132 lat ziemskich

`Sample Input 1:
1000000000
Ziemia`

`Sample Output 1:
31.69`

`Sample Input 2:
2134835688
Merkury`

`Sample Output 2:
280.88`

***

**Zadanie 8**

W pythonie istnieje możliwość tworzenia wirtualnych środowisk za pomocą modułu **virtualenv**. Środowiska wirtualne mają ogromne zastosowanie w Pythonie, ponieważ pozwalają one na organizowanie pakietów dla danego projektu.

Zainstaluj moduł virtualenv oraz stwórz środowisko wirtualne o nazwie **env**.

Następnie w środowisku tym zainstaluj moduł **pandas**.

Uwaga: Należy zainstalować w systemie pakiet **python3-venv**, odpowiedzialny za obsługę środowisk wirtualnych w pythonie.

***