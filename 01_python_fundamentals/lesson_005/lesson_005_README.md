# Lekcja 005: Pętla `for` i `range()`

**Data:** 2026 08 29  
**Etap:** Python Fundamentals  
**Status:** ZALICZONA  
**XP przed lekcją:** 66 / 100  
**XP po lekcji przed commitem:** 83 / 100  
**XP po commicie:** 85 / 100  

## Cel lekcji

Celem było poznanie pętli `for` oraz funkcji `range()` i nauczenie się wykonywania kodu określoną liczbę razy.

## Po co mi ten temat

Pętla `for` jest przydatna wszędzie tam, gdzie chcemy wykonać operację dla kolejnych wartości lub elementów.

1. wykonywanie zadania kilka razy
2. generowanie kolejnych liczb
3. tworzenie tabliczki mnożenia
4. przetwarzanie elementów kolekcji
5. automatyzacja powtarzalnych operacji

## Wymagania wstępne

Przed lekcją potrzebne były:

1. zmienne
2. `input()`
3. `int()`
4. `print()`
5. f string
6. podstawowe działania matematyczne
7. pętla `while`
8. rozumienie iteracji

## Pętla `for`

Najprostszy przykład:

```python
for number in range(5):
    print(number)
```

Wynik:

```text
0
1
2
3
4
```

## Jak działa `range()`

### Jeden argument

```python
range(5)
```

daje:

```text
0
1
2
3
4
```

Liczba końcowa nie należy do zakresu.

### Dwa argumenty

```python
range(2, 6)
```

daje:

```text
2
3
4
5
```

Pierwsza wartość to start.

Druga wartość to stop.

Wartość stop nie jest włączona do zakresu.

### Trzy argumenty

```python
range(2, 10, 2)
```

daje:

```text
2
4
6
8
```

Trzeci argument to krok.

Można go czytać jako:

```text
o ile zmienia się liczba przy każdej iteracji
```

## Odliczanie w dół

```python
for number in range(5, 0, -1):
    print(number)
```

Wynik:

```text
5
4
3
2
1
```

## Zmienna po `for`

W kodzie:

```python
for number in range(1, 5):
    print(number)
```

Python sam przypisuje do `number` kolejne wartości.

Nie trzeba wcześniej pisać:

```python
number = 1
```

To odróżnia typowy sposób użycia `for` od licznika używanego przy `while`.

## Ćwiczenie 1

Program wyświetlający liczby od 1 do 10:

```python
for number in range(1, 11, 1):
    print(number)
```

Wersja uproszczona:

```python
for number in range(1, 11):
    print(number)
```

Krok równy `1` jest domyślny.

## Ćwiczenie 2

Liczby parzyste od 2 do 20:

```python
for number in range(2, 22, 2):
    print(number)
```

Wynik:

```text
2
4
6
8
10
12
14
16
18
20
```

## Ćwiczenie 3

Tabliczka mnożenia dla liczby 5:

```python
number = 5

for multiplier in range(1, 11):
    print(f"Wynik to: {number} x {multiplier} = {multiplier * number}")
```

Najważniejszy wniosek:

```text
number pozostaje stałe
multiplier zmienia się przy każdej iteracji
```

## Zadanie końcowe BEZ AI

Program pobierający liczbę od użytkownika i wyświetlający jej tabliczkę mnożenia od 1 do 10:

```python
number = int(input("Podaj liczbę do mnożenia: "))

for multiplier in range(1, 11):
    print(f"Wynik to: {number} x {multiplier} = {number * multiplier}")
```

Zadanie zostało wykonane samodzielnie.

## Akumulator

Nowy ważny wzorzec pojawił się w końcowym odpytywaniu:

```python
total = 0

for number in range(1, 5):
    total = total + number
    print(total)
```

Wynik:

```text
1
3
6
10
```

## Jak działa `total = total + number`

Przy każdej iteracji Python bierze aktualną wartość `total`, dodaje do niej bieżącą wartość `number` i zapisuje wynik z powrotem do `total`.

Przebieg:

```text
total = 0

number = 1
total = 0 + 1
total = 1

number = 2
total = 1 + 2
total = 3

number = 3
total = 3 + 3
total = 6

number = 4
total = 6 + 4
total = 10
```

To jest wzorzec akumulatora.

## Pytania kontrolne

1. Co robi `for`?
2. Co robi `range(5)`?
3. Dlaczego `range(1, 5)` nie zawiera liczby 5?
4. Co oznacza trzeci argument w `range()`?
5. Jak odliczać w dół?
6. Czy zmienną po `for` trzeba inicjalizować wcześniej?
7. Co oznacza jedna iteracja?
8. Co robi `total = total + number`?
9. Dlaczego `total` może pamiętać wynik z poprzedniej iteracji?

## Typowe błędy i pułapki

1. Oczekiwanie, że stop należy do zakresu
2. Niepotrzebne inicjalizowanie zmiennej po `for`
3. Mylenie bieżącej wartości `number` z wartością akumulatora
4. Nieuwzględnianie kolejności instrukcji
5. Błędne przewidywanie wartości narastającej

## Ocena Lekcji 005

**Logika programistyczna:** 9 / 10  
**Typy i dane:** 9 / 10  
**Składnia:** 9.5 / 10  
**Samodzielność:** 10 / 10  
**Czytanie kodu:** 8.5 / 10  
**Debugowanie:** 9 / 10  
**Wyjaśnianie rozwiązania:** 9 / 10  
**Dekompozycja:** 9 / 10  

Największy mocny punkt:

```text
bardzo szybkie zrozumienie for i range oraz samodzielne napisanie praktycznego zadania
```

Najważniejszy obszar do utrwalenia:

```text
śledzenie wartości akumulatora przez kolejne iteracje
```

## Kryteria zaliczenia

1. [x] Rozumiem podstawową zasadę `for`
2. [x] Rozumiem `range()`
3. [x] Rozumiem start
4. [x] Rozumiem stop
5. [x] Rozumiem krok
6. [x] Potrafię odliczać w dół
7. [x] Potrafię napisać pętlę od 1 do 10
8. [x] Potrafię wygenerować liczby parzyste
9. [x] Potrafię połączyć `for` z mnożeniem
10. [x] Potrafię pobrać dane od użytkownika i użyć ich w pętli
11. [x] Rozumiem podstawę akumulatora

## XP

Pełna lekcja:

```text
10 XP
```

Zadanie bez AI:

```text
5 XP
```

Końcowe odpytywanie:

```text
2 XP
```

Commit po lekcji:

```text
2 XP
```

Stan przed commitem:

```text
83 / 100 XP
```

Stan po commicie:

```text
85 / 100 XP
```

## Status

**Lekcja:** 005  
**Status:** ZALICZONA  
**Etap:** Python Fundamentals  
**Aktualny poziom motywacyjny:** Poziom 1 Start  
**Do Poziomu 2 po commicie:** 15 XP  

## Moje notatki

### Co dziś zrozumiałem

................................................................................

### Co było trudne

................................................................................

### Co chcę powtórzyć

................................................................................

### Moje pytania

................................................................................

## Następna sesja

Sesja 006 będzie checkpointem tygodniowym.

Sprawdzimy bez prowadzenia między innymi:

```text
zmienne
typy danych
input
konwersje
if
elif
else
and
or
not
while
for
range
kolejność instrukcji
akumulator
dekompozycję
```
