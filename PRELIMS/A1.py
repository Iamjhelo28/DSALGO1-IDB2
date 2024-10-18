NintendoWiiprice=100
amount_of_money= int(input("How much money do you have?"))
number= int(amount_of_money / NintendoWiiprice)
afford = NintendoWiiprice - (amount_of_money % NintendoWiiprice)
print("You need an additional ", afford, "to afford a Nintendo Wii")
print("You can buy",number,"pieces of Nintendo Wiis");