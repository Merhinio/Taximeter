
start_price = 4.80
km = int(input("Bitte Kilomenter eingeben: "))
if km > 5: 
    cost = 1.7
else:
    cost = 2.1

totalprice = start_price + km * cost
print('Der Preis beträgt:', totalprice, '€')