# Lekcja 001: Dane, zmienne i pierwszy przepływ programu

**Data:** 2026 08 24  
**Etap:** Python Fundamentals  
**Czas:** około 45 do 60 minut  
**Status:** ZALICZONA  
**Poziom motywacyjny po lekcji:** Poziom 1: Start  
**XP zdobyte:** 19  

## 1. Cel lekcji

Celem pierwszej lekcji było zrozumienie, jak program przechowuje dane, jak rozróżnia podstawowe typy wartości i jak wykonuje instrukcje krok po kroku.

Najważniejszym celem nie było zapamiętanie składni, tylko zbudowanie pierwszego poprawnego modelu działania programu.

## 2. Po co mi ten temat

Prawie każda aplikacja pracuje na danych.

Przykłady:

```text
sklep:
produkt
cena
ilość
klient

ERP:
kontrahent
faktura
kwota
data

AI:
pytanie
odpowiedź
kontekst

backend:
request
użytkownik
status
wynik
```

Zmienne i typy danych są fundamentem wszystkich kolejnych tematów:

* warunków
* pętli
* funkcji
* API
* SQL
* backendu
* automatyzacji
* AI

## 3. Co powinienem umieć po lekcji

* [x] Potrafię utworzyć zmienną
* [x] Rozumiem przypisanie wartości
* [x] Rozróżniam `str`, `int`, `float` i `bool`
* [x] Potrafię użyć zmiennych w obliczeniach
* [x] Rozumiem `print()`
* [x] Rozumiem `input()`
* [x] Wiem, że `input()` zwraca `str`
* [x] Potrafię użyć `int()` i `float()`
* [x] Potrafię przewidzieć wynik prostego kodu
* [x] Potrafię wyjaśnić własny program krok po kroku
* [x] Potrafię użyć prostego f stringa
* [x] Potrafię sformatować liczbę przez `:.2f`

## 4. Zmienne

Przykład:

```python
hourly_rate = 250
```

Tutaj:

```text
hourly_rate
```

to nazwa zmiennej.

```text
=
```

to przypisanie.

```text
250
```

to wartość.

Najlepiej czytać to:

```text
przypisz wartość 250 do zmiennej hourly_rate
```

### Zmiana wartości

```python
price = 100
price = 250
```

Po drugiej instrukcji `price` wskazuje już na `250`.

## 5. Podstawowe typy danych

### `str`

Tekst:

```python
client = "Flora"
```

### `int`

Liczba całkowita:

```python
hours = 5
```

### `float`

Liczba zmiennoprzecinkowa:

```python
price = 250.50
```

### `bool`

Wartość logiczna:

```python
active = True
```

Możliwe wartości:

```python
True
False
```

## 6. Dlaczego typ danych ma znaczenie

```python
5 + 5
```

daje:

```text
10
```

Natomiast:

```python
"5" + "5"
```

daje:

```text
55
```

Dla Pythona liczba i tekst to dwa różne typy.

Podobnie:

```python
"5" * 2
```

daje:

```text
55
```

ponieważ tekst zostaje powtórzony dwa razy.

## 7. `input()`

```python
client = input("Podaj nazwę klienta: ")
```

`input()` zawsze zwraca tekst.

Jeżeli użytkownik wpisze:

```text
10.5
```

to Python początkowo otrzymuje:

```python
"10.5"
```

czyli `str`.

## 8. Konwersja danych

Jeżeli potrzebujemy liczby:

```python
hours = float(input("Podaj liczbę godzin: "))
```

Kolejność:

```text
użytkownik wpisuje "10.5"
input() zwraca "10.5"
float() zamienia "10.5" na 10.5
hours wskazuje na 10.5
```

Dla liczb całkowitych:

```python
age = int(input("Podaj wiek: "))
```

## 9. Ważna różnica

```python
price = "20"
total = int(price) + 5
```

Tutaj `price` nadal jest `str`.

Natomiast:

```python
price = "20"
price = int(price)
```

tutaj `price` wskazuje już na wartość typu `int`.

## 10. Obliczenia i kolejność wykonywania

```python
hours = 5
hourly_rate = 250

total = hours * hourly_rate
```

Python wykonuje:

```text
hours = 5
hourly_rate = 250
5 * 250 = 1250
total = 1250
```

Jeżeli później zmienimy:

```python
hours = 10
```

to `total` nie przeliczy się automatycznie.

To była jedna z najważniejszych zasad tej lekcji:

```text
program wykonuje instrukcje po kolei
wcześniejszy wynik nie przelicza się sam po zmianie innej zmiennej
```

## 11. F string

Przykład:

```python
client = "Flora"
total = 1250

print(f"Klient: {client}, wartość: {total} zł")
```

Wynik:

```text
Klient: Flora, wartość: 1250 zł
```

### Formatowanie do dwóch miejsc

```python
print(f"Wartość: {total:.2f} zł")
```

`:.2f` oznacza wyświetlenie liczby z dwoma miejscami po przecinku.

## 12. Zadanie samodzielne

Program pobierał:

```text
nazwę klienta
liczbę godzin
stawkę godzinową
koszt backupu
```

Finalna wersja:

```python
client = input("Podaj nazwę Klienta: ")
hours = float(input("Podaj liczbę godzin: "))
price = float(input("Podaj stawkę: "))
work = hours * price
backup = float(input("Podaj koszt miesięcznego backupu: "))
total = work + backup

print(
    f"Klient: {client}\n"
    f"Koszt pracy: {work:.2f}\n"
    f"Koszt backupu: {backup:.2f}\n"
    f"Razem: {total:.2f}"
)
```

## 13. Typowe błędy z lekcji

### Próba dodania tekstu do liczby

```python
client + total
```

To nie ma sensu, jeżeli `client` jest `str`, a `total` liczbą.

### Mylenie konwersji z deklaracją typu

`float()` nie deklaruje typu zmiennej na stałe.

Konwertuje konkretną wartość.

### Próba obliczania wartości przed poznaniem potrzebnych danych

Najpierw program musi mieć dane wejściowe, potem może obliczać wynik.

## 14. Pytania kontrolne

1. Co zwraca `input()`?
2. Czym różni się `str` od `int`?
3. Co robi `float()`?
4. Czym różni się `float(price)` od `price = float(price)`?
5. Dlaczego `"5" * 2` daje `"55"`?
6. Co oznacza `:.2f`?
7. Dlaczego zmiana `hours` po obliczeniu `total` nie zmienia automatycznie `total`?
8. Co znajduje się w zmiennej `total` po wykonaniu obliczenia?

## 15. Ocena Lekcji 001

| Obszar | Ocena |
| --- | ---: |
| Logika programistyczna | 9.0 / 10 |
| Typy i dane | 9.5 / 10 |
| Składnia | 8.0 / 10 |
| Samodzielność | 9.5 / 10 |
| Czytanie kodu | 9.0 / 10 |
| Debugowanie | 8.0 / 10 |
| Wyjaśnianie rozwiązania | 8.5 / 10 |

**Ogólna ocena:** 8.8 / 10

## 16. Mocne strony

* szybkie uczenie się na błędach
* dobre wykonywanie kodu w głowie
* samodzielne próby przed proszeniem o pomoc
* dobre rozumienie typów danych
* chęć rozumienia mechanizmu, a nie tylko kopiowania kodu

## 17. Do poprawy

* [ ] Utrwalenie składni
* [ ] Precyzyjniejszy język techniczny
* [ ] Debugowanie bez prowadzenia
* [ ] Utrwalenie różnicy między konwersją a przypisaniem
* [ ] Utrwalenie zachowania operatorów dla różnych typów

## 18. XP

| Aktywność | XP |
| --- | ---: |
| Pełna lekcja | 10 |
| Zadanie bez AI | 5 |
| Końcowe odpytywanie | 2 |
| Commit | 2 |

**Razem:** 19 XP

## 19. Status po lekcji

**Lekcja:** 001  
**Status:** ZALICZONA  
**Seria:** 1 dzień  
**XP:** 19 / 100  
**Najbliższy cel:** warunki i podejmowanie decyzji przez program

## 20. Moje notatki

### Co dziś zrozumiałem

................................................................................

### Co było trudne

................................................................................

### Co chcę powtórzyć

................................................................................

### Moje pytania

................................................................................
