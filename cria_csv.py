import csv

brasil = csv.DictReader(open('municipios-brasil.csv', encoding='utf-8'))
total = {}

for municipio in brasil:
	estado = municipio['estado']
	habitantes = int(municipio['habitantes'])
		
	if estado not in total:
		total[estado] = 0
	total[estado] = total[estado] + habitantes

arquivo = open('habitantes.csv', mode = 'w', encoding = 'utf-8')
resultado = csv.DictWriter(arquivo, fieldnames = ['estado', 'habitantes'])
resultado.writeheader()

for estado, habitantes in total.items():
        resultado.writerow({'estado': estado, 'habitantes': habitantes})
	
