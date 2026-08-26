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
