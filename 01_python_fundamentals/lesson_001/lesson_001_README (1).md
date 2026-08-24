# Lekcja 001: Dane, zmienne i pierwszy przepływ programu

**Data:** 2026 08 24  
**Etap:** Python Fundamentals  
**Czas:** 45 do 60 minut  
**Poziom:** fundamenty  
**Tryb:** teoria, ćwiczenie prowadzone, zadanie samodzielne, odpytywanie, review

## 1. Cel lekcji

Celem jest zrozumienie, jak program przechowuje dane, jak rozróżnia podstawowe typy wartości i jak wykonuje proste instrukcje krok po kroku.

Po tej lekcji powinieneś rozumieć, że prawie każdy program przetwarza dane. Sklep przetwarza produkty, ceny i zamówienia. ERP przetwarza kontrahentów, faktury i kwoty. Aplikacja AI przetwarza pytania, odpowiedzi i dane kontekstowe.

Zmienne są jednym z podstawowych mechanizmów pozwalających programowi pracować na takich danych.

## 2. Po co mi ten temat

Zmienne, typy danych, wejście użytkownika i proste obliczenia są fundamentem praktycznie każdego programu.

Bez tego nie da się sensownie przejść do:

* warunków
* pętli
* funkcji
* API
* SQL
* backendu
* automatyzacji
* AI
* aplikacji webowych

## 3. Co powinienem umieć po lekcji

* [ ] Potrafię utworzyć zmienną
* [ ] Rozumiem, czym jest przypisanie wartości
* [ ] Rozróżniam `str`, `int`, `float` i `bool`
* [ ] Potrafię użyć zmiennych w prostym obliczeniu
* [ ] Rozumiem, co robi `print()`
* [ ] Rozumiem, co robi `input()`
* [ ] Rozumiem, dlaczego `input()` zwraca tekst
* [ ] Potrafię użyć `int()` i `float()` do konwersji danych
* [ ] Potrafię przewidzieć wynik kilku prostych linii kodu
* [ ] Potrafię własnymi słowami wyjaśnić działanie własnego programu

## 4. Zmienna

Na początek można myśleć o zmiennej jak o nazwie przypisanej do wartości.

```python
hourly_rate = 250
```

Tutaj:

`hourly_rate` to nazwa zmiennej.

`=` wykonuje przypisanie.

`250` jest wartością.

Program zapamiętuje więc wartość `250` pod nazwą `hourly_rate`.

Później można wykorzystać tę wartość:

```python
print(hourly_rate)
```

Wynik:

```text
250
```

### Zmiana wartości

```python
hourly_rate = 250
hourly_rate = 300

print(hourly_rate)
```

Wynik:

```text
300
```

Druga instrukcja przypisuje nową wartość do tej samej nazwy.

## 5. Podstawowe typy danych

```python
client = "Flora"
hours = 5
hourly_rate = 250.50
active = True
```

### `str`

Tekst.

```python
client = "Flora"
```

### `int`

Liczba całkowita.

```python
hours = 5
```

### `float`

Liczba z częścią dziesiętną.

```python
hourly_rate = 250.50
```

### `bool`

Wartość logiczna.

```python
active = True
```

Może mieć wartość `True` albo `False`.

## 6. Dlaczego typ ma znaczenie

Te dwie wartości wyglądają podobnie dla człowieka:

```python
number = 5
```

```python
number = "5"
```

Dla Pythona są czymś innym.

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

W drugim przypadku Python łączy dwa teksty.

## 7. Proste obliczenia

```python
hours = 5
hourly_rate = 250

total = hours * hourly_rate
```

### Co komputer robi krok po kroku

1. Zapisuje `5` pod nazwą `hours`
2. Zapisuje `250` pod nazwą `hourly_rate`
3. Odczytuje obie wartości
4. Oblicza `5 * 250`
5. Otrzymuje `1250`
6. Zapisuje `1250` pod nazwą `total`

## 8. `print()`

`print()` służy do wyświetlania danych.

```python
client = "Flora"
print(client)
```

Można też budować czytelne komunikaty:

```python
client = "Flora"
total = 1500

print(f"Klient: {client}, wartość: {total} zł")
```

## 9. `input()`

`input()` pobiera dane wpisane przez użytkownika.

```python
client = input("Podaj nazwę klienta: ")
```

Program zatrzyma się i zaczeka na wpisanie wartości.

### Ważna pułapka

`input()` zwraca tekst.

Jeżeli użytkownik wpisze:

```text
5
```

Python początkowo dostaje:

```python
"5"
```

czyli `str`.

Dlatego często trzeba wykonać konwersję:

```python
hours = int(input("Podaj liczbę godzin: "))
```

Kolejność działania:

1. `input()` pobiera tekst
2. `int()` próbuje zamienić tekst na liczbę całkowitą
3. wynik trafia do `hours`

Dla liczb dziesiętnych używamy:

```python
price = float(input("Podaj cenę: "))
```

## 10. Ćwiczenie prowadzone

Utwórz:

```text
01_python_fundamentals/
    lesson_001/
        basics.py
        exercise.py
```

W `basics.py` wpisz:

```python
name = "Michał"
age = 33
hourly_rate = 250
is_admin = True

print(name)
print(age)
print(hourly_rate)
print(is_admin)
```

Następnie sprawdź typy:

```python
print(type(name))
print(type(age))
print(type(hourly_rate))
print(type(is_admin))
```

### Do sprawdzenia

* [ ] Program uruchamia się bez błędu
* [ ] Rozumiem, dlaczego `name` jest `str`
* [ ] Rozumiem, dlaczego `age` jest `int`
* [ ] Rozumiem, dlaczego `is_admin` jest `bool`

## 11. Ćwiczenie: pierwsze obliczenie

Dodaj:

```python
hours = 5
hourly_rate = 250
```

Samodzielnie utwórz zmienną `total`, która policzy wartość usługi.

Następnie wyświetl wynik.

Potem zmień liczbę godzin na `8`.

Przed uruchomieniem programu przewidź wynik.

## 12. Zadanie samodzielne: kalkulator usługi

### Tryb: BEZ AI

Dozwolone:

* dokumentacja
* sprawdzanie składni
* czytanie błędów
* własne notatki

Niedozwolone:

* generowanie rozwiązania przez ChatGPT
* generowanie rozwiązania przez Claude
* generowanie rozwiązania przez Codex

W `exercise.py` napisz program, który pobiera:

1. nazwę klienta
2. liczbę przepracowanych godzin
3. stawkę godzinową

Program ma policzyć wartość usługi i wyświetlić podsumowanie.

Przykładowe działanie:

```text
Podaj nazwę klienta: Flora
Podaj liczbę godzin: 6
Podaj stawkę godzinową: 250

Klient: Flora
Liczba godzin: 6
Stawka godzinowa: 250 zł
Wartość usługi: 1500 zł
```

### Kryteria

* [ ] Dane są pobierane od użytkownika
* [ ] Liczby są poprawnie konwertowane
* [ ] Program sam wykonuje obliczenie
* [ ] Wynik jest czytelnie wyświetlany
* [ ] Potrafię wyjaśnić każdą linię własnego kodu

## 13. Rozszerzenie zadania

Dodaj miesięczny koszt backupu.

Program ma policzyć:

* koszt pracy
* koszt backupu
* łączny koszt

Przykład danych:

```text
Klient: Granit
Godziny: 8
Stawka: 200
Backup: 350
```

Oczekiwany wynik:

```text
Koszt pracy: 1600 zł
Koszt backupu: 350 zł
Razem: 1950 zł
```

Nie kopiuj gotowego rozwiązania. Sam zdecyduj, jakie zmienne są potrzebne.

## 14. Pytania kontrolne

Odpowiedz własnymi słowami.

1. Czym różni się `int` od `str`?
2. Dlaczego `input()` zwraca tekst?
3. Po co używamy `int()`?
4. Co znajduje się w zmiennej `total`?
5. Co robi operator `*`?
6. Dlaczego `hourly_rate` jest lepszą nazwą niż `x`?
7. Jaka będzie końcowa wartość `price`?

```python
price = 100
price = 200
price = price + 50
```

8. Co wyświetli poniższy kod?

```python
hours = "5"
print(hours * 2)
```

Nie uruchamiaj go przed udzieleniem odpowiedzi.

## 15. Typowe błędy i pułapki

### Mylenie tekstu z liczbą

```python
hours = input("Godziny: ")
```

`hours` jest tutaj tekstem.

### Próba dodania tekstu do liczby

```python
hours = "5"
total = hours + 10
```

To spowoduje błąd typu.

### Nieczytelne nazwy

Słabo:

```python
x = 250
```

Lepiej:

```python
hourly_rate = 250
```

Nazwa powinna pomagać rozumieć kod.

## 16. Kryteria zaliczenia lekcji

Lekcja jest zaliczona, gdy:

* [ ] Potrafię stworzyć kilka zmiennych bez podpowiedzi
* [ ] Rozumiem podstawowe typy danych
* [ ] Potrafię pobrać dane przez `input()`
* [ ] Potrafię zamienić tekst na liczbę
* [ ] Potrafię wykonać proste obliczenie
* [ ] Potrafię przewidzieć wynik prostego kodu
* [ ] Potrafię wyjaśnić własny kod linia po linii
* [ ] Zadanie samodzielne działa
* [ ] Zadanie samodzielne zostało wykonane bez AI

## 17. Czego jeszcze nie muszę umieć

Po tej lekcji nie musisz jeszcze rozumieć:

* warunków
* pętli
* funkcji
* klas
* wyjątków
* bibliotek
* frameworków

Do tych tematów dojdziemy później.

## 18. Git

Po review:

```bash
git status
git add .
git commit -m "Complete lesson 001 Python basics"
git push
```

**Commit:**  
`________________________________________`

## 19. Moje notatki

### Co dziś zrozumiałem

................................................................................

................................................................................

### Co było niejasne

................................................................................

................................................................................

### Co chcę powtórzyć

................................................................................

................................................................................

### Moje pytania

................................................................................

................................................................................

## 20. Status po lekcji

**Lekcja:** 001  
**Status:** do wykonania  
**Seria nauki:** 1 dzień  
**Zadanie bez AI:** do zaliczenia  
**Najbliższy cel:** warunki i podejmowanie decyzji przez program

## 21. Następna lekcja

Po opanowaniu dzisiejszego materiału przejdziemy do warunków logicznych.

Program zacznie nie tylko przechowywać dane i wykonywać obliczenia, ale również podejmować decyzje na podstawie danych.
