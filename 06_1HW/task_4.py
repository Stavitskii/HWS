import validators

pin = input("Enter pin ")
password = input("\nEnter password ")
mail = input("\nEnter mail ")
name = input("\nEnter name ")


print(validators.check_all(pin, password, mail ,name))