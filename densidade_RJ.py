import csv

municipios = csv.DictReader(open('municipios-brasil.csv', encoding='utf-8'))

for municipio in municipios:
    if municipio['estado'] == 'RJ':
        densidade = int(municipio['habitantes']) / float(municipio['area'])
        print(municipio['nome'] + '/RJ' + ': ' + str(densidade) + ' hab/km²')
