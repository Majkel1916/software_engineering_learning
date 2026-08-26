# Lekcja 002: `if`, `elif`, `else` i projektowanie prostego przepływu programu

**Data:** 2026 08 25  
**Etap:** Python Fundamentals  
**Czas:** około 45 do 60 minut  
**Status:** ZALICZONA  
**XP po lekcji i commicie:** 33 / 100  
**Seria:** 2 dni  

## 1. Cel lekcji

Celem było nauczenie programu podejmowania decyzji.

Po Lekcji 001 program potrafił pobierać dane, przechowywać wartości, wykonywać obliczenia i wyświetlać wynik.

Po tej lekcji program potrafi również wybrać różne zachowanie zależnie od danych.

## 2. Po co mi ten temat

Warunki są fundamentem praktycznie każdego systemu.

Przykłady:

```text
jeżeli hasło jest poprawne
przyznaj dostęp
```

```text
jeżeli serwer nie odpowiada
wyślij alert
```

```text
jeżeli wartość zamówienia przekracza próg
nalicz rabat
```

```text
jeżeli użytkownik nie ma uprawnień
odrzuć operację
```

## 3. Co powinienem umieć po lekcji

* [x] Rozumiem `if`
* [x] Rozumiem `elif`
* [x] Rozumiem `else`
* [x] Rozumiem znaczenie wcięć
* [x] Rozumiem kolejność sprawdzania warunków
* [x] Potrafię obsłużyć kilka przedziałów wartości
* [x] Potrafię poprawnie ustawić granice
* [x] Potrafię oddzielić decyzję od późniejszych obliczeń
* [x] Potrafię uniknąć powtarzania tej samej logiki
* [x] Potrafię napisać prostą logikę rabatową

## 4. `if`

Przykład:

```python
balance = 500

if balance >= 300:
    print("Zakup dozwolony")
```

Python sprawdza:

```text
500 >= 300
```

Wynik to `True`, więc wykonuje kod wewnątrz `if`.

## 5. `else`

```python
balance = 299.99

if balance >= 300:
    print("Zakup dozwolony")
else:
    print("Za mało środków")
```

`else` oznacza:

```text
w przeciwnym przypadku
```

## 6. `elif`

```python
score = 85

if score >= 90:
    print("Bardzo dobry")
elif score >= 75:
    print("Dobry")
elif score >= 50:
    print("Dostateczny")
else:
    print("Niezaliczony")
```

Python sprawdza warunki od góry.

Gdy pierwszy pasujący warunek daje `True`, kolejne gałęzie tego samego łańcucha nie są już wykonywane.

## 7. Kolejność warunków ma znaczenie

Źle:

```python
score = 95

if score >= 50:
    print("Dostateczny")
elif score >= 75:
    print("Dobry")
elif score >= 90:
    print("Bardzo dobry")
```

Pierwszy warunek już daje `True`, więc wynik będzie:

```text
Dostateczny
```

## 8. Wcięcia

```python
age = 17

if age < 18:
    print("A")

print("D")
```

Wynik:

```text
A
D
```

`print("D")` wykona się zawsze, ponieważ nie należy do bloku `if`.

W Pythonie wcięcie określa przynależność kodu do bloku.

## 9. Ćwiczenie z wiekiem

```python
age = int(input("Podaj swoj wiek: "))

if age < 18:
    print("Dostęp odrzucony")
elif age <= 64:
    print("Dostęp przyznany")
else:
    print("Dostęp przyznany, senior")
```

### Ważna obserwacja

Nie trzeba pisać:

```python
elif age >= 18 and age <= 64:
```

Jeżeli program dotarł do `elif`, pierwszy warunek `age < 18` już był fałszywy.

## 10. Granice warunków

Założenie:

```text
poniżej 500
brak rabatu

od 500 do poniżej 2000
5 procent

od 2000
10 procent
```

Poprawne warunki:

```python
if total_cost < 500:
    ...
elif total_cost < 2000:
    ...
else:
    ...
```

Dzięki temu:

```text
499.99 → brak rabatu
500    → 5 procent
2000   → 10 procent
```

## 11. Najważniejszy problem Lekcji 002

Pojawiło się zagubienie przy kilku zmiennych:

```text
discount_rate
discount_amount
final_price
```

Kluczowa zasada:

```text
najpierw ustalamy parametr potrzebny do obliczenia
dopiero później wykonujemy obliczenie
```

Nie można policzyć rabatu przed ustaleniem, jaki rabat obowiązuje.

## 12. Poprawny przepływ programu

```text
pobierz dane
ustal discount_rate
policz discount_amount
policz final_price
wyświetl wynik
```

Kod:

```python
client_name = input("Nazwa Klienta: ")
total_cost = float(input("Podaj wartość zamówienia: "))

if total_cost < 500:
    discount_rate = 0
elif total_cost < 2000:
    discount_rate = 0.05
else:
    discount_rate = 0.10

discount_amount = total_cost * discount_rate
final_price = total_cost - discount_amount

print(
    f"Klient: {client_name}\n"
    f"Rabat: {discount_amount:.2f}\n"
    f"Do zapłaty: {final_price:.2f}"
)
```

## 13. Znaczenie zmiennych

### `discount_rate`

Procent rabatu:

```python
0
0.05
0.10
```

### `discount_amount`

Konkretna kwota rabatu:

```python
discount_amount = total_cost * discount_rate
```

### `final_price`

Cena po rabacie:

```python
final_price = total_cost - discount_amount
```

## 14. Ważna zasada kolejności

Błędna koncepcja:

```text
policz wynik
potem zmień discount_rate
oczekuj, że wcześniejszy wynik przeliczy się sam
```

Poprawnie:

```text
ustal discount_rate
potem policz wynik
```

Python wykonuje kod po kolei.

Zmiana zmiennej nie przelicza automatycznie wcześniejszych wyników.

## 15. Dekompozycja problemu

Przed większym zadaniem warto zapisać po polsku:

```text
Dane wejściowe

Decyzja

Obliczenia

Wynik
```

Przykład:

```text
Dane wejściowe:
nazwa klienta
wartość zamówienia

Decyzja:
jaki rabat obowiązuje

Obliczenia:
kwota rabatu
cena końcowa

Wynik:
podsumowanie dla użytkownika
```

## 16. Typowe błędy

### Zła granica

```python
if total_cost <= 500:
```

dla wymagania:

```text
od 500 zł obowiązuje rabat
```

byłoby błędne.

### Zła nazwa zmiennej

Jeżeli nazwa nie odpowiada temu, co faktycznie przechowuje zmienna, kod staje się trudniejszy do czytania.

### Drugi niepotrzebny `if`

Jeżeli pierwszy `if` już ustalił `discount_rate`, nie trzeba drugi raz sprawdzać tych samych progów tylko po to, aby wyświetlić wynik.

## 17. Pytania kontrolne

1. Kiedy używamy `if`?
2. Czym różni się `elif` od osobnego `if`?
3. Co oznacza `else`?
4. Dlaczego kolejność warunków ma znaczenie?
5. Co oznacza wcięcie w Pythonie?
6. Dlaczego `discount_amount` liczymy po `if`, a nie przed nim?
7. Czym różni się `discount_rate` od `discount_amount`?
8. Dlaczego testujemy `499.99`, `500` i `2000`?
9. Dlaczego drugi zestaw identycznych warunków był zbędny?

## 18. Ocena Lekcji 002

| Obszar | Ocena |
| --- | ---: |
| Logika programistyczna | 8.5 / 10 |
| Warunki | 9.5 / 10 |
| Składnia | 8.5 / 10 |
| Samodzielność | 9.5 / 10 |
| Czytanie kodu | 9.0 / 10 |
| Debugowanie | 8.5 / 10 |
| Projektowanie zmiennych | 8.0 / 10 |

**Ogólna ocena:** około 8.7 / 10

## 19. Największy progres

Pod koniec lekcji kod został uproszczony do struktury:

```text
decyzja
obliczenie
prezentacja
```

To był pierwszy krok od:

```text
kod działa
```

do:

```text
kod jest logicznie uporządkowany
```

## 20. Największy słaby punkt

Najtrudniejsza była dekompozycja oraz kolejność operacji.

Wniosek:

```text
gdy problem zaczyna się komplikować
najpierw rozpisz go po polsku
dopiero potem twórz zmienne i kod
```

## 21. Poziom pomocy

Zadanie końcowe wymagało około:

```text
Poziom pomocy 2
```

czyli wskazówki koncepcyjnej.

Cel na przyszłość:

```text
podobne zadanie za kilka tygodni
Poziom pomocy 0 albo 1
```

## 22. XP

Stan po lekcji i commicie:

```text
33 / 100 XP
```

## 23. Status po lekcji

**Lekcja:** 002  
**Status:** ZALICZONA  
**Seria:** 2 dni  
**XP:** 33 / 100  
**Poziom:** Poziom 1 Start  
**Najbliższy cel:** warunki złożone i logika boolowska  
**Najbliższy checkpoint:** sobota  

## 24. Moje notatki

### Co dziś zrozumiałem

................................................................................

### Co było trudne

................................................................................

### Co chcę powtórzyć

................................................................................

### Moje pytania

................................................................................
