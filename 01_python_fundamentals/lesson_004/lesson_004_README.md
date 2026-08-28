# Lekcja 004: Pętla `while`

**Data:** 2026 08 28  
**Etap:** Python Fundamentals  
**Status:** ZALICZONA  
**XP przed lekcją:** 52 / 100  
**XP po lekcji przed commitem:** 64 / 100  
**XP po commicie:** 66 / 100  

## Cel lekcji

Celem było zrozumienie, jak program może wykonywać ten sam fragment kodu wielokrotnie, dopóki określony warunek pozostaje prawdziwy.

## Po co mi ten temat

Pętle są potrzebne wszędzie tam, gdzie program ma powtarzać czynność.

1. Ponawianie pytania o hasło
2. Obsługa kilku prób logowania
3. Przetwarzanie kolejnych elementów danych
4. Powtarzanie zadania do momentu spełnienia warunku
5. Automatyzacja operacji wykonywanych wielokrotnie

## Wymagania wstępne

Przed tą lekcją potrzebne były:

1. zmienne
2. `if`
3. `else`
4. `and`
5. `==`
6. `!=`
7. operatory porównania
8. `True` i `False`

## Nowe pojęcie: `while`

`while` można czytać jako:

```text
dopóki
```

Przykład:

```python
counter = 1

while counter <= 3:
    print(counter)
    counter = counter + 1
```

Program wyświetli:

```text
1
2
3
```

## Co komputer robi krok po kroku

Na początku:

```python
counter = 1
```

Python sprawdza:

```python
counter <= 3
```

Dla wartości `1` wynik to `True`.

Program wykonuje wnętrze pętli:

```python
print(counter)
counter = counter + 1
```

Po pierwszej iteracji:

```text
counter = 2
```

Python ponownie sprawdza warunek.

Proces trwa do chwili, gdy:

```text
counter = 4
```

Wtedy:

```python
4 <= 3
```

daje:

```text
False
```

i pętla się kończy.

## Iteracja

Jedno wykonanie wnętrza pętli nazywamy iteracją.

Jeżeli pętla wykonała swój blok trzy razy, miała trzy iteracje.

## Infinite loop

Przykład:

```python
counter = 1

while counter <= 3:
    print(counter)
```

Tutaj `counter` nigdy się nie zmienia.

Warunek:

```python
counter <= 3
```

zawsze pozostaje prawdziwy.

Program będzie więc wykonywał pętlę bez końca.

Najważniejsze pytanie przy `while`:

```text
Co sprawi, że warunek kiedyś stanie się False?
```

## Ćwiczenie z licznikiem

Kod napisany samodzielnie:

```python
counter = 1

while counter < 6:
    print(counter)
    counter = counter + 1

print("Done")
```

Wynik:

```text
1
2
3
4
5
Done
```

## Ćwiczenie z hasłem bez limitu prób

Kod napisany samodzielnie:

```python
password = "python123"

input_password = input("Podaj swoje haslo: ")

while input_password != password:
    input_password = input("Podaj swoje haslo: ")

print("Witamy, hasło poprawne")
```

## Zadanie końcowe: trzy próby logowania

Finalna wersja:

```python
password = "python123"
counter = 1

input_password = input("Podaj swoje haslo: ")
print(counter)

while input_password != password and counter < 3:
    input_password = input("Podaj swoje haslo: ")
    counter += 1
    print(counter)

if input_password == password:
    print("Welcome!")
else:
    print("Dupa! nie udało się ;/")
```

## Dekompozycja rozwiązania

Dane wejściowe:

```text
hasło użytkownika
```

Stan początkowy:

```text
poprawne hasło
liczba wykorzystanych prób
```

Warunek pętli:

```text
hasło jest niepoprawne
oraz
liczba prób jest mniejsza niż 3
```

Zmiana stanu:

```text
pobranie kolejnego hasła
zwiększenie licznika prób
```

Zakończenie:

```text
poprawne hasło
albo
wykorzystanie limitu prób
```

Wynik:

```text
dostęp przyznany
albo
dostęp odrzucony
```

## Ważna pułapka z kolejnością instrukcji

Kod:

```python
counter = 1

while counter < 4:
    counter += 1
    print(counter)

print("Koniec")
```

wyświetli:

```text
2
3
4
Koniec
```

Nie wyświetli `1`, ponieważ najpierw wykonuje się:

```python
counter += 1
```

a dopiero potem:

```python
print(counter)
```

## Pytania kontrolne

1. Co oznacza `while`?
2. Czym jest iteracja?
3. Co może spowodować infinite loop?
4. Dlaczego zmienna używana w warunku często musi zmieniać się wewnątrz pętli?
5. Kiedy pętla `while` się kończy?
6. Dlaczego kolejność `counter += 1` i `print(counter)` ma znaczenie?
7. Jak połączyć warunek hasła i limit prób za pomocą `and`?
8. Co dzieje się po wyjściu z pętli?

## Typowe błędy i pułapki

1. Brak zmiany wartości używanej w warunku
2. Zła granica warunku
3. Mylenie liczby iteracji z końcową wartością licznika
4. Nieuwzględnianie kolejności instrukcji
5. Zakładanie, że wartość zostanie wydrukowana przed jej zmianą
6. Brak sprawdzenia wyniku po zakończeniu pętli

## Ocena Lekcji 004

**Logika programistyczna:** 9 / 10  
**Typy i dane:** 9 / 10  
**Składnia:** 9.5 / 10  
**Samodzielność:** 9.5 / 10  
**Czytanie kodu:** 8 / 10  
**Debugowanie:** 9 / 10  
**Wyjaśnianie rozwiązania:** 8.5 / 10  
**Dekompozycja:** 9 / 10  

Największy mocny punkt:

```text
szybkie zrozumienie mechanizmu while i samodzielne wykorzystanie go w praktycznym zadaniu
```

Najważniejszy obszar do utrwalenia:

```text
dokładne śledzenie kolejności instrukcji i końcowej wartości zmiennych
```

## Kryteria zaliczenia

1. [x] Rozumiem podstawową zasadę `while`
2. [x] Rozumiem iterację
3. [x] Rozumiem infinite loop
4. [x] Potrafię zmieniać licznik
5. [x] Potrafię określić warunek zakończenia
6. [x] Potrafię połączyć `while` z `and`
7. [x] Potrafię połączyć `while` z `if`
8. [x] Potrafię napisać prosty system limitu prób
9. [x] Rozumiem znaczenie kolejności instrukcji

## XP

Pełna lekcja:

```text
10 XP
```

Końcowe odpytywanie:

```text
2 XP
```

Commit po lekcji:

```text
2 XP
```

Zadanie końcowe nie otrzymuje dodatkowych 5 XP za tryb bez AI, ponieważ podczas rozwiązania wykorzystano wskazówki szkoleniowe.

Stan przed commitem:

```text
64 / 100 XP
```

Stan po commicie:

```text
66 / 100 XP
```

## Status

**Lekcja:** 004  
**Status:** ZALICZONA  
**Etap:** Python Fundamentals  
**Aktualny poziom motywacyjny:** Poziom 1 Start  
**Następny cel:** Lekcja 005  

## Moje notatki

### Co dziś zrozumiałem

................................................................................

### Co było trudne

................................................................................

### Co chcę powtórzyć

................................................................................

### Moje pytania

................................................................................

## Następna lekcja

Na początku Lekcji 005 zostanie krótko sprawdzona retencja:

```text
while
iteracja
warunek zakończenia
zmiana stanu
kolejność instrukcji
```

Dopiero potem zostanie wprowadzony kolejny temat.
