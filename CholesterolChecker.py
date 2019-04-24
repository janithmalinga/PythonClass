ldl = float(input ("Enter LDL : "))
hdl = float(input ("Enter HDL : "))
tri = float(input ("Enter TRI : "))

total = ldl + hdl + (tri/5)

if (ldl<100) and (hdl > 60 ) and (tri<150) and (total<200):
    print("good")
elif (ldl>=100 and ldl <= 130) and (hdl >= 50 and hdl <= 60 ) and (tri>=150 and tri<=200) and (total>=200 and total<=240):
    print("Boardline")
else:
    ("bad")