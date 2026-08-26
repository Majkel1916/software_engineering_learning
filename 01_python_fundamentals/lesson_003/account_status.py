status = input("Podaj status konta: ")

if status == "active":
    print("Konto aktywne")
elif status == "blocked":
    print("Konto zablokowane")
else:
    print("Nieznany status")
