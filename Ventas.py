import random
from SemanaCompra import *

numeramdon = 0
while True:
    numeramdon = random.randint(1000000, 9999999)
    break

codigoVenta = f'FA2026-{numeramdon}'

#Todas las semanas en funcion al calendario
ReportesVentasTotal = {
    'junio': {
        'semana 1': week1,
        
        'semana 2': week2,
        
        'semana 3': week3,
        
        'semana 4': week4
    }
}