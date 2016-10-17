from random import randint
nev=input("Hogy hívnak?")
print("szia " + nev)
print("Gondoltam egy számra 1 és 100 között, találd ki!")
x=randint(1,100) 

for n in range(1, 10):	
	y=int(input(str(n) + ". tipp?"))
	if y == x:
		print("Király vagy!")
		break
	elif y < x:
		print("A gondolt szám nagyobb")
	else:
		print("A gondolt szám kisebb")

print(x)
