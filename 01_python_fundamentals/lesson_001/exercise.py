client = input("Podaj nazwę Klienta: ")
hours = int(input("Podaj liczbe godzin: "))
price_hourly = float((input("Podaj stawke: ")))

total = hours * price_hourly

print(f"Klient: {client} wartość usługi: {total:.2f} zł")
