# Checkpoint tygodniowy 001

**Data:** 5 września 2026
**Etap roadmapy:** Python Fundamentals
**Status:** ZALICZONY
**Tryb:** zadanie praktyczne BEZ AI oraz odpytywanie
**XP po checkpointcie:** 61 XP
**Poziom motywacyjny:** Poziom 1 Start

## Cel checkpointu

Sprawdzenie, czy potrafię samodzielnie połączyć podstawowe elementy Pythona w działający program.

## Zakres

1. Zmienne

2. `input()`

3. `float()`

4. Operacje matematyczne

5. `if`

6. `elif`

7. `else`

8. `and`

9. `or`

10. `=`

11. `==`

12. Pętle

13. `range()`

14. Formatowanie f string

## Zadanie praktyczne

Program przygotowujący wycenę usługi IT.

Dane wejściowe:

```python
name = input("Wpisz nazwę Klienta: ")
hours = float(input("Podaj liczbę godzin: "))
price = float(input("Podaj stawkę godzinową: "))
VIP = input("Czy Klient jest VIP? Wpisz Yes lub No: ")
```

Logika rabatu:

```python
if VIP == "Yes" and final_price >= 1000:
    discount_rate = 0.1
    rabat = 10
elif final_price >= 1000:
    discount_rate = 0.05
    rabat = 5
else:
    discount_rate = 0
    rabat = 0
```

Obliczenie rabatu:

```python
discount_amount = final_price * discount_rate
```

Formatowanie wyników:

```python
print(f"Koszt przed rabatem: {hours * price:.2f} zł")
print(f"Rabat: {rabat} procent")
print(f"Kwota rabatu {discount_amount:.2f} zł")
print(f"Do zapłaty: {final_price - discount_amount:.2f} zł")
```

## Co komputer robi krok po kroku

Najpierw pobiera dane.

Potem zamienia godziny i stawkę na liczby.

Następnie oblicza koszt pracy.

Potem sprawdza warunki rabatowe od najbardziej szczegółowego.

Jeżeli klient jest VIP i koszt spełnia próg, wybierany jest rabat 10 procent.

Jeżeli klient nie spełnia warunku VIP, ale koszt przekracza próg, wybierany jest rabat 5 procent.

W pozostałych przypadkach rabat wynosi 0 procent.

Dopiero po wybraniu stawki rabatu program oblicza jego wartość.

Na końcu odejmuje rabat od ceny i prezentuje wynik.

## Testy

### Test 1

Flora, 10 godzin, 250 zł, VIP.

Wynik:

```text
2500.00 zł
10 procent
250.00 zł rabatu
2250.00 zł do zapłaty
```

Status: poprawny.

### Test 2

2 godziny, 200 zł, brak VIP.

Wynik:

```text
400.00 zł
0 procent
400.00 zł do zapłaty
```

Status: poprawny.

### Test 3

5 godzin, 250 zł, brak VIP.

Wynik:

```text
1250.00 zł
5 procent
62.50 zł rabatu
1187.50 zł do zapłaty
```

Status: poprawny.

## Typowe błędy i pułapki

`range()` nie zawiera wartości końcowej.

Przy `if`, `elif`, `else` Python wykonuje pierwszą pasującą gałąź.

Warunek bardziej szczegółowy powinien znaleźć się przed bardziej ogólnym, jeśli ten ogólny również mógłby go spełnić.

`=` oznacza przypisanie.

`==` oznacza porównanie.

Stawka rabatu musi być znana przed obliczeniem kwoty rabatu.

Nazwy zmiennych powinny odpowiadać temu, co faktycznie przechowują.

## Kryteria zaliczenia

[x] samodzielne napisanie programu

[x] poprawne pobieranie danych

[x] poprawna konwersja danych

[x] poprawne warunki

[x] poprawne użycie `and`

[x] prawidłowa kolejność operacji

[x] poprawne obliczenie rabatu

[x] poprawne formatowanie pieniędzy

[x] trzy poprawne testy

[x] wyjaśnienie własnej logiki

## Ocena

Logika programistyczna: 9 na 10

Typy i dane: 9 na 10

Składnia: 8.5 na 10

Samodzielność: 9.5 na 10

Czytanie kodu: 8.5 na 10

Debugowanie: 8.5 na 10

Wyjaśnianie rozwiązania: 9 na 10

## Mocne strony

Warunki logiczne.

Samodzielność.

Rozumienie `and` i `or`.

Kolejność obliczeń.

Rozumienie zależności pomiędzy danymi.

## Do dalszej pracy

Precyzyjne śledzenie pętli.

`range()`.

Nazewnictwo zmiennych.

Debugowanie bardziej złożonych błędów.

## Commit Git

Commit:

`____________________________`

## Własne notatki

`____________________________`

## Pytania i rzeczy do powtórki

`____________________________`

## Następny krok

Dzień 7.

Dalsze rozwijanie fundamentów Pythona oraz stopniowe przechodzenie od pojedynczych instrukcji do kodu, który potrafimy dzielić na logiczne części.
