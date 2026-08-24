client = input("Podaj nazwę Klienta: ")
hours = float(input("Podaj liczbę godzin: "))
price = float(input("Podaj stawkę: "))
work = hours * price
backup = float(input("Podaj koszt miesięcznego backupu: "))
total = work + backup


print(f"Klient: {client}\nKoszt pracy: {work:.2f}\nKoszt backupu: {backup:.2f}\nRazem: {total:.2f}")
