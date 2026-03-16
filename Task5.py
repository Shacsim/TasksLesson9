summa = float(input("Omonat summasini kiriting: "))
if summa < 100000:
    foiz = summa * 0.05
    print(f"Omonat summasi {summa} so'm, foiz miqdori {foiz} so'm.")
elif 100000 <= summa <= 500000:
    foiz = summa * 0.07
    print(f"Omonat summasi {summa} so'm, foiz miqdori {foiz} so'm.")
else:
    foiz = summa * 0.10
    print(f"Omonat summasi {summa} so'm, foiz miqdori {foiz} so'm.")
