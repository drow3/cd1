import sys

def kiiras(nev):
	print('hello ' + nev)


nev = 'vilag'
if(len(sys.argv) == 2):
	nev = sys.argv[1]
elif(len(sys.argv) > 2):
	print("Maximum 1 nev adhato meg.")
	sys.exit(2)
kiiras(nev)
