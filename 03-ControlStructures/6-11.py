oryginalna_cena_produktu = 200
cena_produktu_po_obniżce = 190
obniżka = (oryginalna_cena_produktu - cena_produktu_po_obniżce) / oryginalna_cena_produktu * 100
print(f"Obniżka jest równa {obniżka} %")
if(obniżka >= 10):
    print("Kup produkt!")