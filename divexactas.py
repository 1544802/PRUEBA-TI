flag1=True
flag2=True
while flag1:
     try:
         a=int(input("valor 1:"))
         flag1=False
     except ValveError:
         print("te equivocaste")
print("termine el primer lood")
while flag2:
	 try:
	 	b=int(input("valor 2:"))
	 	flag2=False
     except ValveError:
     	print("te equivocaste")
print("termine el segundo lood")
print(f"si los datos obtenidos son {a} {b}")

def die(a,b):
	if(a%b)==0:
	   r=f"{a} / {b} es exacta"
	elif (a%b)==2:
		r=f"{a} / {b} es inexacta"
	return r
	