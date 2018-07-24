import codecs, sys
with open(sys.argv[1]) as file:
	ff = file.read().split('\n')
	header = ff[0]
	dna = ''.join(ff[1:])
trlib = {'A': 'А', 'C': 'Ц', 'G':'Г', 'T':'Т'}
newdna = ''
for i in range(len(dna)):
	newdna = newdna + trlib[dna[i]]
print(header)
print(newdna)
