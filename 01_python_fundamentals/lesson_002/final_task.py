client_name = input("Nazwa Klienta: ")
total_cost = float(input("Podaj wartość zamówienia: "))

if total_cost < 500:
    discount_rate = 0
elif total_cost < 2000:
    discount_rate = 0.05
else:
    discount_rate = 0.10

discount_amount = total_cost * discount_rate
final_price = total_cost - discount_amount

print (f"Klienta: {client_name}\nRabat: {discount_amount:.2f}\nDo zapłaty: {final_price:.2f}")





