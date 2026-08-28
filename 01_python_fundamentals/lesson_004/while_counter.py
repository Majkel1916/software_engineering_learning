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



