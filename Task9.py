tomon1 = float(input("Birinchi tomon: "))
tomon2 = float(input("Ikkinchi tomon: "))
tomon3 = float(input("Uchinchi tomon: "))
if tomon1 == tomon2 == tomon3:
    print("Uchburchak teng tomonli.")
elif tomon1 == tomon2 or tomon1 == tomon3 or tomon2 == tomon3:
    print("Uchburchak teng yonli.")
else:
    print("Uchburchak turli tomonli.")
    