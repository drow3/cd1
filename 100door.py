print ("hello") 

ajto_list = ['zarva']*100
	
for n in range (1,100):
	
	for j in range(n,100,n):
	
		if ajto_list[j] == 'zarva':
				ajto_list[j] = 'nyitva'	
		
		elif ajto_list[j] == 'nyitva':
				ajto_list[j] = 'zarva'
			

for x in range (1,100):
	if ajto_list[x] == 'nyitva':
		print (x)

	

