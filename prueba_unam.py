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
    df = pd.read_excel(
        'assets/ASISTENCIA_DERECHO_AGRARIO_UNAM_2022.xlsx', skiprows=3)
    # df['cuenta'] = df['NUMERO DE CUENTA'] agregar nueva columna
    return df


def getDataCsv():
    df = pd.read_csv('assets/participants_85620635684.csv')
    return df


def getCsvAlumnos():
    df = getDataCsv()
    alumnosPresentes = df['Nombre (nombre original)'][1:].str.upper().tolist()
    trans_tab = dict.fromkeys(map(ord, u'\u0301\u0308'), None)

    for x in range(0, len(alumnosPresentes)):
        alumnosPresentes[x] = normalize('NFKC', normalize(
            'NFKD', alumnosPresentes[x]).translate(trans_tab))

        if alumnosPresentes[x] == 'BALCAZAR CERVANTES MARIA GUADALUPE (LUUU)':
            alumnosPresentes[x] = 'BALCAZAR CERVANTES MARIA GUADALUPE'
        if alumnosPresentes[x] == 'PEREZ CARRILLO ARELI PAOLA (ARELI PAOLA PEREZ CARRILLO)':
            alumnosPresentes[x] = 'PEREZ CARRILLO ARELI PAOLA'
        if alumnosPresentes[x] == 'JOCELYN MACHUCA':
            alumnosPresentes[x] = 'MACHUCA JIMENEZ JOCELYN'
        if alumnosPresentes[x] == 'MONICA CASTILLO':
            alumnosPresentes[x] = 'CASTILLO DURAN MONICA'
        if alumnosPresentes[x] == 'KARLA ESTRADA':
            alumnosPresentes[x] = 'ESTRADA GOMEZ KARLA LIZETH'
        if alumnosPresentes[x] == 'SILVA SALAZAR DIANA LIZBETH (DIANA LIZBETH SILVA SALAZAR)':
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
        if alumnosPresentes[x] == 'ANA XIMENA VELAZQUEZ PADRON (ANA PADRON)':
            alumnosPresentes[x] = 'VELAZQUEZ PADRON ANA XIMENA'
        if alumnosPresentes[x] == 'AZUCENA CHAVARRIA SALAS':
            alumnosPresentes[x] = 'CHAVARRIA SALAS AZUCENA'
        if alumnosPresentes[x] == 'DANIELA SERRANO':
            alumnosPresentes[x] = 'SERRANO RODRIGUEZ DANIELA'
        if alumnosPresentes[x] == 'ENRIQUE CRUZ ROMERO':
            alumnosPresentes[x] = 'CRUZ ROMERO ENRIQUE'
        if alumnosPresentes[x] == 'GARCIA ROBLES FERNANDA':
            alumnosPresentes[x] = 'GARCIA ROBLES MARIA FERNANDA SIDNEY'
        if alumnosPresentes[x] == 'GERARDO MENDOZA':
            alumnosPresentes[x] = 'MENDOZA GARCIA GERARDO'
        if alumnosPresentes[x] == 'JOCELYN MACHUCA JIMENEZ':
            alumnosPresentes[x] = 'MACHUCA JIMENEZ JOCELYN'
        if alumnosPresentes[x] == 'SANCHEZ CALIXTO JUAN CARLOS (43 - SANCHEZ CALIXTO JUAN CARLOS)':
            alumnosPresentes[x] = 'SANCHEZ CALIXTO JUAN CARLOS'
        if alumnosPresentes[x] == 'VICTORIA DANIEL HUITRON':
            alumnosPresentes[x] = 'DANIEL HUITRON SARAH BELEN'
        if alumnosPresentes[x] == 'ARRIAGA GLORIA ALEJANDRA RCJE':
            alumnosPresentes[x] = 'ARRIAGA GLORIA ALEJANDRA'

    alumnosPresentes.sort()

    return alumnosPresentes


def generar_asistencia():

    # ruta de nuestro archivo
    filesheet = "./assets/ASISTENCIA_DERECHO_AGRARIO_UNAM_2022.xlsx"

    # creamos el objeto load_workbook
    wb = openpyxl.load_workbook(filesheet)

    # Seleccionamos el archivo
    sheet = wb.active

    # seleccionamos el rango de celdas de los alumnos
    rango1 = sheet['C5:C52']

    # max_row
    # for i in rango1:
    print(rango1[0])

    # print(type(rango1)) 

    # Guardamos el archivo con los cambios
    # wb.save(filesheet)


def init():
    # fecha_clase = input('Introduce la fecha de la clase: ')
    # print(fecha_clase)

    generar_asistencia()


init()
