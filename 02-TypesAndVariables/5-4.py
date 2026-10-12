Amount = input("Jaka kwota? ")
float_Amount = float(Amount)
VAT = float_Amount * 23 / 100
round_VAT = round(VAT,2)
print(f'Amount  :   {float_Amount}')
print(f'VAT 23% :   {round_VAT}')