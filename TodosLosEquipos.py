import PyPDF2
import pandas as pd
import calendar
import locale


locale.setlocale(locale.LC_TIME,'es_ES')

femenino="/Users/jenarofg/Python/ExtraerPDF/femenino.pdf"
juvenil="/Users/jenarofg/Python/ExtraerPDF/juvenil.pdf"
cadete="/Users/jenarofg/Python/ExtraerPDF/cadete.pdf"
infantila="/Users/jenarofg/Python/ExtraerPDF/infantila.pdf"
infantilb="/Users/jenarofg/Python/ExtraerPDF/infantilb.pdf"
alevina="/Users/jenarofg/Python/ExtraerPDF/alevina.pdf"
alevinb="/Users/jenarofg/Python/ExtraerPDF/alevinb.pdf"
benjamina="/Users/jenarofg/Python/ExtraerPDF/benjamina.pdf"
benjaminb="/Users/jenarofg/Python/ExtraesrPDF/benjaminb.pdf"
prebenjamin="/Users/jenarofg/Python/ExtraerPDF/prebenjamin.pdf"
#Buenas
#DEFINICION DE DICCIONARIO CON EQUIPOS 
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
        'C.D. Arenal ':['EL TRAGAMON 2','Gijón','H.Sintética','Campo'],
        'Cimadevilla C.F.':['POLIDEPORTIVO NATAHOYO','Gijón','H.Sintética','Campo'],
        'Real Avilés Industrial C.F. SAD':['campo','Avilés','H.Sintética','Campo'],
        'Rayo Gijonés':['campoMAXIMINO MARTÍNEZ Nº1','Gijón','H.Sintética','Campo'],
        'Urraca C.F.':['LA CORREDORIA','Posada de Llanes','H.Sintética','Campo'],
        'Club Atletico de la Ribera':['EL LLOSALIN ','Soto del Rey','H.Natural','Campo'],
        'U.D. Llanera':['PEPE QUIMARAN','Posada de Llanera','H.Sintética','Campo'],
        'Deportiva Piloñesa':['LA COVIELLA','Villamayor','H.Natural','Campo'],
        'L''Entregu C.F.':['NUEVO NALON','San Martin del Rey Aurelio','H.Sintética','Campo'],
        'C.D. Llanes':['LA ENCARNACION','Llanes','H.Sintética','Campo'],
        'Fortuna C.F.':['MUNICIPAL ARRIONDAS','Parres','H.Sintética','Campo']}
    if valor in diccionario_equipos:
        return diccionario_equipos[valor]
    else:
        return diccionarioEquipos('')

#FUNCION QUE RECIBE UN TEXTO Y AÑADA A LAS LISTAS PASADAS LOS VALORES CORRESPONDIENTES
def separarfecha(fecha,dia,mes):
    for fechas in fecha:
        fechaseparada=fechas.split('-')
        #mesnom=calendar.month_name(int(fechaseparada[1]))
        #print(calendar.month_name[2])
        dia.append(fechaseparada[0])
        mes.append(calendar.month_name[int(fechaseparada[1])])


def principal(equipo,categoria):
    ljornadas,lfechas,llocal,lvisitante,campo,ciudad,tcesped,ldia,lmes=[],[],[],[],[],[],[],[],[]
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
                        campo.append("Perlora")
                        ciudad.append("Perlora")
                        tcesped.append("H.Natural")
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
    separarfecha(lfechas,ldia,lmes)
    lmesmayus=[elemento.upper() for elemento in lmes]
    llocalmayus=[elemento.upper() for elemento in llocal]
    lvisitantemayus=[elemento.upper() for elemento in lvisitante]
    df=pd.DataFrame()
    df['Jornada']=ljornadas
    df['Dia']=ldia
    df['Mes']=lmesmayus
    df['Local']=llocal
    df['Visitante']=lvisitante
    df['Campo']=campo
    df['Ciudad']=ciudad
    df['Tipo de cesped']=tcesped
    df_ordenado=df.sort_values(by='Jornada')
    
    print(df_ordenado)


principal(cadete,"CADETE")
principal(femenino,"FEMENINO")
principal(juvenil,"JUVENIL")
principal(infantila,"INFANTIL A")
principal(infantilb,"INFANTIL B")
principal(alevina,"ALEVIN A")
principal(alevinb,"ALEVIN B")
principal(benjamina,"BENJAMIN A")


