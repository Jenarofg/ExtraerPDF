import PyPDF2
import pandas as pd
import calendar
import locale
from datetime import date
import sqlite3



locale.setlocale(locale.LC_TIME,'es_ES')

femenino="/Users/jenarofg/Python/ExtraerPDF/ExtraerPDF/Calendarios/femenino.pdf"
juvenil="/Users/jenarofg/Python/ExtraerPDF/ExtraerPDF/Calendarios/juvenil.pdf"
cadete="/Users/jenarofg/Python/ExtraerPDF/ExtraerPDF/Calendarios/cadete.pdf"
infantila="/Users/jenarofg/Python/ExtraerPDF/ExtraerPDF/Calendarios/infantila.pdf"
infantilb="/Users/jenarofg/Python/ExtraerPDF/ExtraerPDF/Calendarios/infantilb.pdf"
alevina="/Users/jenarofg/Python/ExtraerPDF/ExtraerPDF/Calendarios/alevina.pdf"
alevinb="/Users/jenarofg/Python/ExtraerPDF/ExtraerPDF/Calendarios/alevinb.pdf"
benjamina="/Users/jenarofg/Python/ExtraerPDF/ExtraerPDF/Calendarios/benjamina.pdf"
benjaminb="/Users/jenarofg/Python/ExtraerPDF/ExtraerPDF/Calendarios/benjaminb.pdf"
prebenjamin="/Users/jenarofg/Python/ExtraerPDF/ExtraerPDF/Calendarios/prebenja.pdf"


def diccionarioEquipos(valor):
    diccionario_equipos={'':['','','',''],
        'U.D. Gijon Industrial':['SANTA CRUZ','Gijón','H.Sintética','Campo'],
        'Grupo Deportivo Bosco':['SANTO DOMINGO','Aviles','H.Sintética','Campo'],
        'A.D. Lloreda':['LLOREDA','Tremañes','H.Sintética','Campo'],
        'S.D.At. Camocha':['MUNICIPAL VEGA','Gijón','H.Sintética','Campo'],
        'C.D. Raices':['RAIMUNDO ALVAREZ','Raices','H.Sintética','Campo'],
        'Colegio de La Inmaculada':['COLEGIO INMACULADA','Gijón','H.Sintética','Campo'],
        'Escuela de Futbol Jin':['MAXIMINO MARTÍNEZ Nº2','Gijón','H.Sintética','Campo'],
        'C.D. La Braña':['EL MORTERO','Gijón','H.Sintética','Campo'],
        'Navarro C.F. Alusin Solar':['TABIELLA 2','Aviles','H.Sintética','Campo'],
        'Veriña C.F.':['LLOREDA','Gijón','H.Sintética','Campo'],
        'Escuela Futbol Mareo':['MAREO 6','Gijón','H.Sintética','Campo'],
        'C.D. Manuel Rubio':['LOS PERICONES','Gijón','H.Sintética','Campo'],
        'Atlantic Gijón':['ANGEL REY','Gijón','H.Natural','Campo'],
        'Codema':['EL CLARET','Gijón','H.Natural','Campo'],
        'C.D. Deva':['CAMPO LA LABORAL','Gijón','H.Sintética','Campo'],
        'Asunción C.F.':['CAMPO LA LABORAL','Gijón','H.Sintética','Campo'],
        'C.D. San Julian de Roces':['BRAÑA SUR','Gijón','H.Sintética','Campo'],
        'C.D. Montevil':['MONTEVIL','Gijón','H.Sintética','Campo'],
        'C.D. Quirinal':['LA TOBA 1','Avilés','H.Sintética','Campo'],
        'C.D. Lealtad de Villaviciosa':['NUEVO VILLAZON','Villaviciosa','H.Sintética','Campo'],
        'Atl. del Llano C.F.':['BRAÑA SUR','Gijón','H.Sintética','Campo'],
        'Unión Astur C.F.':['MAXIMINO MARTÍNEZ Nº1 ','Gijón','H.Sintética','Campo'],
        'C.D. Gijón Perchera F.S.':['EL MORTERO','Gijón','H.Sintética','Campo'],
        'Cultural Deportiva de Aboño':['GOMEZ LOZANA','Aboño','H.Natural','Campo'],
        'Gijon Futbol Femenino':['MAXIMINO MARTÍNEZ Nº2','Gijón','H.Sintética','Campo'],
        'Peña C.D. Hermanos Castro':['MAXIMINO MARTÍNEZ Nº2','Gijón','H.Sintética','Campo'],
        'C.F. Estudiantes':['NUEVO SAN JULIAN','Gijón','H.Natural','Campo'],
        'Fabril C.D.':['SANTA CRUZ','Gijón','H.Sintética','Futbol8'],
        'C.D. Arenal':['EL TRAGAMON 2','Gijón','H.Sintética','Campo'],
        'Cimadevilla C.F.':['POLIDEPORTIVO NATAHOYO','Gijón','H.Sintética','Campo'],
        'Real Avilés Industrial C.F. SAD':['campo','Avilés','H.Sintética','Campo'],
        'Rayo Gijonés':['campoMAXIMINO MARTÍNEZ Nº1','Gijón','H.Sintética','Campo'],
        'Urraca C.F.':['LA CORREDORIA','Posada de Llanes','H.Sintética','Campo'],
        'Club Atletico de la Ribera':['EL LLOSALIN ','Soto del Rey','H.Natural','Campo'],
        'U.D. Llanera':['PEPE QUIMARAN','Posada de Llanera','H.Sintética','Campo'],
        'Deportiva Piloñesa':['LA COVIELLA','Villamayor','H.Natural','Campo'],
        'L''Entregu C.F.':['NUEVO NALON','San Martin del Rey Aurelio','H.Sintética','Campo'],
        'C.D. Llanes':['LA ENCARNACION','Llanes','H.Sintética','Campo'],
        'Fortuna C.F.':['MUNICIPAL ARRIONDAS','Parres','H.Sintética','Campo'],
        'S.D. Cancienes':['POLIDEPORTIVO CANCIENES','Corvera','Pista','Pista']}
    if valor in diccionario_equipos:
        return diccionario_equipos[valor]
    else:
        return diccionarioEquipos('')
    
def separarfecha(fecha,dia,mes,fecha_objeto):
    for fechas in fecha:
        fechaseparada=fechas.split('-')
        #mesnom=calendar.month_name(int(fechaseparada[1]))
        #print(calendar.month_name[2])
        fecha_objeto.append(date(int(fechaseparada[2]),int(fechaseparada[1]),int(fechaseparada[0])))
        dia.append(fechaseparada[0])
        mes.append(calendar.month_name[int(fechaseparada[1])])

def selecVictoria(categoria,campo,ciudad,tcesped):
    selVictoria={'FEMENINO':['PERLORA','PERLORA','H.NATURAL'],
                 'JUVENIL':['ANEXO LA MATA','CANDÁS','H.NATURAL'],
                 'CADETE':['PERLORA','PERLORA','H.NATURAL'],
                 'INFANTIL A':['PERLORA','PERLORA','H.NATURAL'],
                 'INFANTIL B':['PERLORA','PERLORA','H.NATURAL'],
                 'ALEVIN A':['ANEXO LA MATA','CANDÁS','H.SINTETICA'],
                 'ALEVIN B':['ANEXO LA MATA','CANDÁS','H.SINTETICA'],
                 'BENJAMIN A':['POLIDEPORTIVO CANDÁS','CANDÁS','PISTA'],
                 'BENJAMIN B':['POLIDEPORTIVO CANDÁS','CANDÁS','PISTA'],
                 'PREBENJAMIN':['POLIDEPORTIVO CANDÁS','CANDÁS','PISTA']}
    
    campo.append(selVictoria[categoria][0])
    ciudad.append(selVictoria[categoria][1])
    tcesped.append(selVictoria[categoria][2])


def principal(equipo,categoria,ljornadas,lfechas,llocal,lvisitante,campo,ciudad,tcesped,ldia,lmes):
    with open(equipo,"rb") as archivo:
        lector_pdf=PyPDF2.PdfReader(archivo)
        numeroPag=len(lector_pdf.pages)
        limite = (lambda x: 2 if x == 4 else 3)(numeroPag)
        for page in range(1,limite):
            pag_obt=lector_pdf.pages[page]
            text=pag_obt.extract_text()
            linea=text.split('\n')
            for line in linea:
                if "Jornada" in line:
                    posicionJornada=line.find("Jornada")
                    textoJornada=line[posicionJornada:]
                    fecha=textoJornada.split()
                    ljornadas.append(int(fecha[1]))
                    lfechas.append(fecha[2].strip("()"))
                if "Club Victoria" in line:
                    partes=line.split("-")
                    if "Club Victoria" in partes[0]:
                        selecVictoria(categoria,campo,ciudad,tcesped)
                    else:
                        visit=partes[0]
                        posicionComilla=visit.find('"')
                        vistsincomillas=visit[:posicionComilla].strip()
                        numeroreg=len(campo)
                        e=diccionarioEquipos(vistsincomillas)
                        if e[0]!='':
                            campo.append(e[0])
                            ciudad.append(e[1])
                            tcesped.append(e[2])
                        else:
                            campo.append("")
                            ciudad.append("")
                            tcesped.append("")                   
                    if partes[0].split(' "A"')[0]=="Club Victoria" or partes[0].split(' "B"')[0]=="Club Victoria":
                        llocal.append(categoria)
                    else:
                        llocal.append(partes[0])
                    if partes[1].split(' "A"')[0]=="Club Victoria"=="Club Victoria" or partes[1].split(' "B"')[0]=="Club Victoria":
                        lvisitante.append(categoria)
                    else:
                        lvisitante.append(partes[1])
    

ljornadas,lfechas,llocal,fecha_objeto,lvisitante,campo,ciudad,tcesped,ldia,lmes=[],[],[],[],[],[],[],[],[],[]
principal(cadete,"CADETE",ljornadas,lfechas,llocal,lvisitante,campo,ciudad,tcesped,ldia,lmes)
principal(juvenil,"JUVENIL",ljornadas,lfechas,llocal,lvisitante,campo,ciudad,tcesped,ldia,lmes)
principal(infantila,"INFANTIL A",ljornadas,lfechas,llocal,lvisitante,campo,ciudad,tcesped,ldia,lmes)
principal(infantilb,"INFANTIL B",ljornadas,lfechas,llocal,lvisitante,campo,ciudad,tcesped,ldia,lmes)
principal(alevina,"ALEVIN A",ljornadas,lfechas,llocal,lvisitante,campo,ciudad,tcesped,ldia,lmes)
principal(alevinb,"ALEVIN B",ljornadas,lfechas,llocal,lvisitante,campo,ciudad,tcesped,ldia,lmes)
principal(benjamina,"BENJAMIN A",ljornadas,lfechas,llocal,lvisitante,campo,ciudad,tcesped,ldia,lmes)
principal(benjaminb,"BENJAMIN B",ljornadas,lfechas,llocal,lvisitante,campo,ciudad,tcesped,ldia,lmes)
principal(prebenjamin,"PREBENJAMIN",ljornadas,lfechas,llocal,lvisitante,campo,ciudad,tcesped,ldia,lmes)
separarfecha(lfechas,ldia,lmes,fecha_objeto)
llocal=[elemento.upper() for elemento in llocal]
lvisitante=[elemento.upper() for elemento in lvisitante]
lmesmayus=[elemento.upper() for elemento in lmes]
llocalmayus=[elemento.upper() for elemento in llocal]
lvisitantemayus=[elemento.upper() for elemento in lvisitante]
campo= [elemento.upper() for elemento in campo]
ciudad=[elemento.upper() for elemento in ciudad]
tcesped=[elemento.upper() for elemento in tcesped]

df=pd.DataFrame()
df['Jornada']=ljornadas
df['Fecha']=fecha_objeto
df['Dia']=ldia
df['Mes']=lmesmayus
df['Local']=llocal
df['Visitante']=lvisitante
df['Campo']=campo
df['Ciudad']=ciudad
df['Tipo de cesped']=tcesped


#PRUEBA BASE DE DATOS

class PartidosDB:
    def __init__(self, ljornadas, fecha_objeto, ldia, lmesmayus, llocal, lvisitante, campo, ciudad, tcesped):
        self.df = pd.DataFrame({
            'Jornada': ljornadas,
            'Fecha': fecha_objeto,
            'Dia': ldia,
            'Mes': lmesmayus,
            'Local': llocal,
            'Visitante': lvisitante,
            'Campo': campo,
            'Ciudad': ciudad,
            'Tipo de cesped': tcesped
        })
    
    def guardar_en_sqlite(self, nombre_bd='mi_base_de_datos.sqlite', nombre_tabla='partidos'):
        # Conectar a la base de datos SQLite (o crearla si no existe)
        conexion = sqlite3.connect(nombre_bd)
        
        # Escribir el DataFrame en una tabla
        self.df.to_sql(nombre_tabla, conexion, if_exists='replace', index=False)
        
        # Cerrar la conexión
        conexion.close()

# Crear una instancia de la clase y guardar los datos en SQLite
partidos_db = PartidosDB(ljornadas, fecha_objeto, ldia, lmesmayus, llocal, lvisitante, campo, ciudad, tcesped)
partidos_db.guardar_en_sqlite("/Users/jenarofg/Python/ExtraerPDF/bdpartidos.sqlite","partidos")
print("Calendario guardado en bdpartidos.sqlite")
    


#Se ordena por fecha de partido
#df_ordenado=df.sort_values(by='Fecha')
#print(df_ordenado)
#Filtor para obtener solo los partidos como local.
#filtro = df_ordenado[df_ordenado['Local'].isin(['CADETE', 'JUVENIL','INFANTIL A','INFANTIL B','ALEVIN A','ALEVIN B','BENJAMIN A','BENJAMIN B','PREBENJAMIN'])]
#print(filtro)
print(df)


# Aplicar el estilo al DataFrame
#df_styled=filtro.style.set_properties(**{"border": "2px solid blue", "color": "black"})

# Guardar el DataFrame estilizado en un archivo HTML
#df_styled.to_html('/Users/jenarofg/Python/ExtraerPDF/styled_dataframe.html')

#filtro.to_csv('/Users/jenarofg/Python/ExtraerPDF/TodosCasa.csv', index=False)

