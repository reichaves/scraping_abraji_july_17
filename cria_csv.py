import csv

brasil = csv.DictReader(open('municipios-brasil.csv', encoding='utf-8'))
total = {}

for municipio in brasil:
	estado = municipio['estado']
	habitantes = int(municipio['habitantes'])
		
	if estado not in total:
		total[estado] = 0
	total[estado] = total[estado] + habitantes

# I use below a context manager. It's the word "with" in python. What this syntax does, in the case of files is to execute the close () method on the object as soon as the code exits the indentation. Tip by Guilherme Marthe

with open('habitantes.csv', mode = 'w', encoding = 'utf-8') as arquivo:
        resultado = csv.DictWriter(arquivo, fieldnames = ['estado', 'habitantes'])
        resultado.writeheader()

        for estado, habitantes in total.items():
                resultado.writerow({'estado': estado, 'habitantes': habitantes})
	
# If you run your code from REPL (IDLE, ipython, or python itself) the file will not close and the changes will not be 'flushed' to the file.
# So just add the line arquivo.close() at the end of your script and the changes will be written to your file.
