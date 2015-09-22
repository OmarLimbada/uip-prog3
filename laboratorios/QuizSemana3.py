b = 5
a = 7
are_cm = (a * b)
peri_cm = (2*a) + (2*b)
are_m = are_cm / 100
peri_m = peri_cm / 100
are_pulg = are_cm / 2.54
peri_pulg = peri_cm / 2.54
print("area = " + str(are_cm) +"cm" + " Perimetro = " + str(peri_cm) +"cm" )
print("area = " + str(are_m) +"m" + " Perimetro = " + str(peri_m) +"m" )
print("area = " + str(are_pulg) +"pulg" + " Perimetro = " + str(peri_pulg) +"pulg")