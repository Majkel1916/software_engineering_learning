name = input("Wpisz nazwę Klienta: ")
hours = float(input("Podaj liczbę godzin: "))
price = float(input("Podaj stawkę godzinową: " ))
VIP = input("Czy Klient jest VIP? - Wpisz Yes/No: ")
final_price = price * hours


if VIP == "Yes" and final_price >= 1000:
    discount_rate = 0.1
    rabat = 10
elif final_price >= 1000:
    discount_rate = 0.05
    rabat = 5
else:
    discount_rate = 0
    rabat = 0

discount_amount = final_price * discount_rate

print(f"Koszt przed rabatem: {final_price:.2f} zł")
print(f"Rabat: {rabat} procent")
print(f"Kwota rabatu {discount_amount:.2f} zł")
print (f"Do zapłaty: {final_price-discount_amount:.2f} zł")









