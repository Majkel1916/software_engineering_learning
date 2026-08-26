# Lekcja 003: Warunki złożone, bool, `and`, `or`, `not`, `==`, `!=`

**Data:** 2026 08 26  
**Etap:** Python Fundamentals  
**Czas:** sesja rozpoczęta jako minimum 15 minut, następnie rozszerzona do pełnej lekcji  
**Status:** ZALICZONA  
**Poziom motywacyjny:** Poziom 1: Start  
**XP przed lekcją:** 33 / 100  
**XP po lekcji przed commitem:** 50 / 100  
**XP po commicie:** 52 / 100  
**Seria:** 3 dni  

## 1. Cel lekcji

Celem lekcji było nauczenie programu podejmowania decyzji na podstawie kilku warunków jednocześnie.

Po wcześniejszych lekcjach program potrafił już:

* przechowywać dane
* pobierać dane od użytkownika
* konwertować typy
* wykonywać obliczenia
* używać `if`, `elif` i `else`

W tej lekcji doszły warunki złożone oraz wartości logiczne.

## 2. Po co mi ten temat

Warunki złożone występują praktycznie w każdej prawdziwej aplikacji.

Przykłady:

```text
użytkownik może się zalogować,
jeżeli konto jest aktywne
i nie jest zablokowane
```

```text
klient dostaje dostęp,
jeżeli jest pełnoletni
i ma aktywne konto
i spełnia dodatkowe wymaganie biznesowe
```

```text
administrator może wejść do panelu,
jeżeli jest administratorem
lub właścicielem
```

Te same mechanizmy pojawią się później w backendzie, API, systemach autoryzacji, walidacji danych, automatyzacjach i regułach biznesowych.

## 3. Co powinienem umieć po lekcji

* [x] Rozumiem wartości `True` i `False`
* [x] Rozumiem, czym jest typ `bool`
* [x] Rozumiem różnicę między `=` i `==`
* [x] Rozumiem operator `!=`
* [x] Potrafię użyć `and`
* [x] Potrafię użyć `or`
* [x] Rozumiem działanie `not`
* [x] Potrafię połączyć kilka warunków w jednym `if`
* [x] Rozumiem znaczenie nawiasów w warunkach złożonych
* [x] Potrafię przed kodowaniem rozpisać dane wejściowe, decyzję i wynik
* [x] Potrafię napisać prosty system autoryzacji bez gotowego rozwiązania AI

## 4. `bool`

Typ `bool` może mieć jedną z dwóch wartości:

```python
True
False
```

Przykład:

```python
age = 20
result = age >= 18

print(result)
```

Python sprawdza:

```text
20 >= 18
```

Wynik:

```text
True
```

Czyli `result` wskazuje na wartość logiczną `True`.

## 5. Operator przypisania `=` a porównanie `==`

### Przypisanie

```python
status = "active"
```

Czytamy:

```text
przypisz wartość "active" do status
```

### Porównanie

```python
status == "active"
```

Czytamy:

```text
czy status jest równy "active"?
```

Porównanie daje wynik `True` albo `False`.

## 6. Operator `!=`

`!=` oznacza:

```text
różne od
```

Przykład:

```python
status = "active"

if status != "blocked":
    print("Można się zalogować")
```

Python sprawdza:

```text
"active" != "blocked"
```

Wynik to `True`.

## 7. Operator `and`

`and` oznacza:

```text
wszystkie warunki muszą być prawdziwe
```

Przykład:

```python
age = 20
account_active = True

if age >= 18 and account_active:
    print("Dostęp przyznany")
```

Analiza:

```text
age >= 18        → True
account_active   → True

True and True    → True
```

Jeżeli jeden warunek jest `False`:

```text
True and False   → False
```

### Reguła

```text
and = wszystkie wymagania muszą być spełnione
```

## 8. Operator `or`

`or` oznacza:

```text
wystarczy przynajmniej jeden prawdziwy warunek
```

Przykład:

```python
is_admin = False
is_owner = True

if is_admin or is_owner:
    print("Dostęp przyznany")
```

Analiza:

```text
False or True → True
```

### Reguła

```text
or = wystarczy jeden prawdziwy wariant
```

## 9. Operator `not`

`not` odwraca wartość logiczną.

```python
account_disabled = True

print(not account_disabled)
```

Wynik:

```text
False
```

Czyli:

```text
not True  → False
not False → True
```

Przykład praktyczny:

```python
blocked = False

if not blocked:
    print("Dostęp przyznany")
```

Można to przeczytać:

```text
jeżeli użytkownik NIE jest zablokowany
```

## 10. Warunki złożone

Przykład:

```python
age = 20
status = "active"
vip = False
order_value = 1500

if age >= 18 and (status == "active" or vip):
    print("Dostęp przyznany")
```

Najpierw analizujemy nawias:

```text
status == "active" → True
vip                → False

True or False      → True
```

Następnie:

```text
age >= 18          → True

True and True      → True
```

Wynik:

```text
Dostęp przyznany
```

## 11. Ważna zasada: najpierw logika po polsku

Przed napisaniem większego warunku warto rozpisać problem.

Przykład z zadania końcowego:

```text
Dane wejściowe:

wiek
status konta
wartość zamówienia
status VIP


Warunki:

wiek minimum 18

ORAZ

konto aktywne

ORAZ

zamówienie minimum 1000
LUB
status VIP


Wynik:

Dostęp przyznany
albo
Dostęp odrzucony
```

Dopiero później tłumaczymy to na Python.

## 12. Ćwiczenie: status konta

Kod napisany samodzielnie:

```python
status = input("Podaj status konta: ")

if status == "active":
    print("Konto aktywne")
elif status == "blocked":
    print("Konto zablokowane")
else:
    print("Nieznany status")
```

## 13. Zadanie końcowe

### Tryb

**BEZ AI do generowania rozwiązania**

Program pobiera:

```text
wiek
status konta
wartość zamówienia
informację VIP
```

Dostęp jest przyznany tylko wtedy, gdy:

```text
wiek >= 18

AND

status == "active"

AND

wartość zamówienia >= 1000
OR
VIP
```

### Rozwiązanie napisane samodzielnie

```python
age = int(input("Podaj wiek: "))
status = input("Podaj status: ")
summary_order = float(input("Podaj wartość zamówienia: "))
vip = input("Czy jesteś VIP: ")

if vip == "yes":
    vip = True
else:
    vip = False

if age >= 18 and status == "active" and (summary_order >= 1000 or vip):
    print("Dostęp przyznany")
else:
    print("Dostęp odrzucony")
```

## 14. Co można później poprawić

Nazwa:

```python
summary_order
```

jest mniej czytelna niż:

```python
order_value
```

Docelowo preferujemy:

```python
order_value = float(input("Podaj wartość zamówienia: "))
```

Można również później uprościć:

```python
if vip == "yes":
    vip = True
else:
    vip = False
```

ponieważ samo porównanie:

```python
vip == "yes"
```

już daje `True` albo `False`.

## 15. Ważny błąd z końcowego odpytywania

Kod:

```python
age = 17
status = "active"
order_value = 5000
vip = True

result = age >= 18 and status == "active" and (order_value >= 1000 or vip)

print(result)
```

Pierwsza odpowiedź była:

```text
nic się nie wyświetli
```

To było niepoprawne.

### Poprawna analiza

```text
age >= 18                  → False
status == "active"         → True
order_value >= 1000        → True
vip                        → True
True or True               → True

False and True and True    → False
```

`result` otrzymuje więc:

```python
False
```

A ponieważ:

```python
print(result)
```

wykonuje się bezwarunkowo, wynik to:

```text
False
```

### Wniosek

Trzeba rozróżniać:

```text
wartość warunku jest False
```

od:

```text
kod znajduje się wewnątrz if i dlatego nie zostaje wykonany
```

## 16. Retencja z poprzedniej lekcji

Poprawnie zapamiętana została najważniejsza zasada z Lekcji 002:

```text
najpierw ustalamy discount_rate
dopiero później liczymy discount_amount
```

Powód:

```text
program musi najpierw znać właściwy procent,
żeby mógł policzyć konkretną kwotę rabatu
```

Ocena retencji tego elementu:

**10 / 10**

## 17. Ocena Lekcji 003

| Obszar | Ocena | Wniosek |
| --- | ---: | --- |
| Logika programistyczna | 9.5 / 10 | Bardzo dobre łączenie kilku warunków |
| Warunki złożone | 9.5 / 10 | Poprawne wykorzystanie `and`, `or` i nawiasów |
| `and`, `or`, `not` | 9.0 / 10 | Mechanizm rozumiany poprawnie |
| `bool` i porównania | 9.0 / 10 | Dobre rozumienie `True`, `False`, `==`, `!=` |
| Składnia | 9.0 / 10 | Wyraźna poprawa względem Lekcji 001 |
| Samodzielność | 10 / 10 | Zadanie końcowe napisane samodzielnie |
| Dekompozycja problemu | 9.5 / 10 | Wyraźna poprawa względem Lekcji 002 |
| Czytanie kodu | 8.5 / 10 | Jeden ważny błąd dotyczący `print(result)` |

**Ogólna ocena Lekcji 003:** 9.2 / 10

**Status:** ZALICZONA

## 18. Największy progres

W Lekcji 002 pojawiło się zagubienie przy większej liczbie zmiennych i kolejności operacji.

W Lekcji 003 przed napisaniem kodu problem został najpierw rozpisany jako:

```text
dane wejściowe
warunki
wynik
```

Dopiero później powstał kod.

To przełożyło się na poprawnie napisany złożony warunek:

```python
if age >= 18 and status == "active" and (summary_order >= 1000 or vip):
```

## 19. Co trzeba utrwalić

* [ ] Różnicę między `False` jako wynikiem a niewykonaniem kodu wewnątrz `if`
* [ ] Precyzyjne czytanie `>=` zamiast `>`
* [ ] Precyzyjne techniczne tłumaczenie warunków
* [ ] Dalsze ćwiczenie dekompozycji przed kodowaniem
* [ ] Nazewnictwo zmiennych

## 20. Kryteria zaliczenia

* [x] Rozumiem `bool`
* [x] Rozumiem `True` i `False`
* [x] Rozumiem `and`
* [x] Rozumiem `or`
* [x] Rozumiem `not`
* [x] Rozumiem `==`
* [x] Rozumiem `!=`
* [x] Potrafię połączyć kilka warunków
* [x] Potrafię zastosować nawiasy w warunku złożonym
* [x] Potrafię rozpisać problem przed napisaniem kodu
* [x] Potrafię samodzielnie napisać prostą regułę autoryzacyjną

## 21. XP

Lekcja rozpoczęła się jako sesja minimum, ale została rozszerzona do pełnej lekcji.

Nie sumujemy punktów za minimum i pełną lekcję jednocześnie.

| Aktywność | XP |
| --- | ---: |
| Pełna lekcja | 10 |
| Zadanie bez gotowego rozwiązania AI | 5 |
| Końcowe odpytywanie | 2 |
| Commit | 2 po wykonaniu |

**XP przed Lekcją 003:** 33

**XP przed commitem:** 50

**XP po commicie:** 52 / 100

## 22. Status kursu

**Dzień:** 3  
**Seria:** 3 dni  
**Etap:** Python Fundamentals  
**Lekcje zaliczone:** 3  
**Poziom motywacyjny:** Poziom 1: Start  
**XP po commicie:** 52 / 100  
**Do Poziomu 2 Fundamenty:** 48 XP  
**Najbliższy checkpoint:** sobota  
**Status planu 9 miesięcy:** zgodnie z planem  

## 23. Moje notatki

### Co dziś zrozumiałem

................................................................................

................................................................................

### Co było trudne

................................................................................

................................................................................

### Co chcę powtórzyć

................................................................................

................................................................................

### Moje pytania

................................................................................

................................................................................

## 24. Następna lekcja

Na początku kolejnej sesji zostanie sprawdzona retencja:

```text
and
or
not
==
!=
False jako wartość
kod wykonywany warunkowo
```

Następnie przejdziemy do kolejnego elementu Python Fundamentals zgodnie z roadmapą.
