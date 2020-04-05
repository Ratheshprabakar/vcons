def vowels(input_string):
	"""
	To count the number of vowels in a string
	"""
	count=0
	for i in input_string:
		if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
			count=count+1
	return count
def consonants(input_string):
	"""
	To count the number of consonants in a string
	"""
	count=0
	for i in input_string:
		if(i!='a' and i!='e' and i!='i' and i!='o' and i!='u' and i!='A' and i!='E' and i!='I' and i!='O' and i!='U'):
			if (i.isalpha()):
				count=count+1
	return count

