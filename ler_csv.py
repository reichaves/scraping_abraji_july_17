#import csv

#pops = csv.DictReader(open("MUN_FXQ_3550308_2050.csv", encoding='latin-1'))

#print("Como será São Paulo daqui 50 anos, por faixa etária")
#print()

#for numeros in pops:
#    print(numeros["Faixa_Etaria_Quinquenal"] + "/" + numeros["Total"])

    
import csv

municipios = csv.DictReader(open("municipios-brasil.csv", encoding='utf-8'))

for municipio in municipios:
    print(municipio["nome"] + "/" + municipio["estado"])
