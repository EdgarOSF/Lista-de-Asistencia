import pandas as pd
import openpyxl
import re
from unicodedata import normalize
import csv

from alumnos import alumnos 

# skiprows:  ignorar una o más filas
# names[]: nombre concreto para cada una de las columnas, difernte al de la hoja

# listaAlumnos =


def getDataExcel():
    df = pd.read_excel('LISTAS DE ASISTENCIA-UNAM.xlsx', skiprows=3)
    # df['cuenta'] = df['NUMERO DE CUENTA'] agregar nueva columna
    return df


def getAlumnosListaUnam():
    df = pd.read_excel(
        'LISTAS DE ASISTENCIA-UNAM.xlsx',
        skiprows=3
    )
    alumnos = df.NOMBRE

    return alumnos


def getDataCsv():
    df = pd.read_csv('participants_82348827697.csv', encoding='latin-1')
    return df
    # with open('participants_82348827697.csv', 'rb') as f:
        # text = f.read()
        # text = f.read().decode(errors='replace')
    # return text


def getCsvAlumnos():
    df = pd.read_csv('participants_82348827697.csv')
    alumnosPresentes = df['Nombre (nombre original)'][1:].str.upper().tolist()
    trans_tab = dict.fromkeys(map(ord, u'\u0301\u0308'), None)

    for x in range(0, len(alumnosPresentes)):
        alumnosPresentes[x] = normalize('NFKC', normalize(
            'NFKD', alumnosPresentes[x]).translate(trans_tab))

        if alumnosPresentes[x] == 'LUUU':
            alumnosPresentes[x] = 'BALCAZAR CERVANTES MARIA GUADALUPE'
        if alumnosPresentes[x] == 'PEREZ CARRILLO ARELI PAOLA (ARELI PAOLA PEREZ CARRILLO)':
            alumnosPresentes[x] = 'PEREZ CARRILLO ARELI PAOLA'
        if alumnosPresentes[x] == 'JOCELYN MACHUCA':
            alumnosPresentes[x] = 'MACHUCA JIMENEZ JOCELYN'
        if alumnosPresentes[x] == 'MONICA CASTILLO':
            alumnosPresentes[x] = 'CASTILLO DURAN MONICA'
        if alumnosPresentes[x] == 'KARLA ESTRADA':
            alumnosPresentes[x] = 'ESTRADA GOMEZ KARLA LIZETH'
        if alumnosPresentes[x] == 'LIZBETH SILVA':
            alumnosPresentes[x] = 'SILVA SALAZAR DIANA LIZBETH'
        if alumnosPresentes[x] == 'STEPHANIA RIVAS':
            alumnosPresentes[x] = 'RIVAS GARCIA STEPHANIA ARACELI'
        if alumnosPresentes[x] == 'FERNANDO VERDUZCO':
            alumnosPresentes[x] = 'VERDUZCO MATEO JORGE FERNANDO'
        if alumnosPresentes[x] == 'ROSA ALINE BARBOSA RODRIGUEZ (BARBOSA RODRIGUEZ ALINE)':
            alumnosPresentes[x] = 'BARBOSA RODRIGUEZ ROSA ALINE'
        if alumnosPresentes[x] == 'JAVIER CANSECO':
            alumnosPresentes[x] = 'CANSECO MARTINEZ JAVIER EDUARDO'
        if alumnosPresentes[x] == 'OMAR MEZA':
            alumnosPresentes[x] = 'MEZA SAMANIEGO OMAR ALBERTO'
        if alumnosPresentes[x] == 'ALEXIS EDUARDO PRADO MEJIA':
            alumnosPresentes[x] = 'PRADO MEJIA ALEXIS EDUARDO'
        if alumnosPresentes[x] == 'DOLORES DEL CARMEN GARCIA CRUZ':
            alumnosPresentes[x] = 'GARCIA CRUZ DOLORES DEL CARMEN'
        if alumnosPresentes[x] == 'GABRIELA MENDOZA FLORES':
            alumnosPresentes[x] = 'MENDOZA FLORES GABRIELA'
        if alumnosPresentes[x] == 'JONATHAN BECERRIL':
            alumnosPresentes[x] = 'BECERRIL CRUZ JONATHAN ROMAN'
        if alumnosPresentes[x] == 'JUAN CARLOS MARQUEZ MENDOZA':
            alumnosPresentes[x] = 'MARQUEZ MENDOZA JUAN CARLOS'
        if alumnosPresentes[x] == 'LUZ SABINE MONTAÑO JIMMEN':
            alumnosPresentes[x] = 'MONTAÑO JIMMEN LUZ SABINE'
        if alumnosPresentes[x] == 'MARIA GUADALUPE RUIZ GONZALEZ':
            alumnosPresentes[x] = 'RUIZ GONZALEZ MARIA GUADALUPE'
        if alumnosPresentes[x] == 'MARIANA ARELI SANTOS OSNAYA':
            alumnosPresentes[x] = 'SANTOS OSNAYA MARIANA ARELI'
        if alumnosPresentes[x] == 'MARYPAZ MARTINEZ GONZALEZ':
            alumnosPresentes[x] = 'MARTINEZ GONZALEZ MARYPAZ'
        if alumnosPresentes[x] == 'OBED MONTAÑO CRUZ':
            alumnosPresentes[x] = 'MONTAÑO CRUZ OBED ANTONIO'
        if alumnosPresentes[x] == 'YANNELI BOLAÑOS MOYA':
            alumnosPresentes[x] = 'BOLAÑOS MOYA MARIA YANNELI'

    alumnosPresentes.sort()

    return alumnosPresentes


# print(getCsvAlumnos())
# print(getAlumnosListaUnam())
# print(getDataCsv())

print(alumnos)
