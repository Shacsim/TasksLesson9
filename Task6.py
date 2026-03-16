raqam = input("Telefon raqamingizni kiriting:(masalan XXxxxXXxx formatda) ")
if len(raqam) == 9 and raqam[0:2] == "90" or raqam[0:2] == "91":
    print(f"Telefon raqam {raqam} Beeline operatoriga tegishli.")
elif len(raqam) == 9 and raqam[0:2] == "93" or raqam[0:2] == "94":
    print(f"Telefon raqam {raqam} Ucell operatoriga tegishli.")
elif len(raqam) == 9 and raqam[0:2] == "97" or raqam[0:2] == "88":
    print(f"Telefon raqam {raqam} Mobiuz operatoriga tegishli.")
elif len(raqam) == 9 and raqam[0:2] == "99" or raqam[0:2] == "95":
    print(f"Telefon raqam {raqam} Uztelecom operatoriga tegishli.")
else:
    print("Telefon raqam noto'g'ri formatda kiritilgan yoki operator kodi noto'g'ri.")  
