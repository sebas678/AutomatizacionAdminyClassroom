from __future__ import print_function
from datetime import datetime
import csv

import os.path
from unicodedata import name

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/admin.directory.user',
'https://www.googleapis.com/auth/admin.directory.group',
'https://www.googleapis.com/auth/admin.directory.orgunit']

def consultaAlumno(mail):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    service = build('admin', 'directory_v1', credentials=creds)

    try:
        user=service.users().get(userKey=mail).execute()
        print("")
        print(user['id'],user['name']['givenName'],user['name']['familyName'],user['lastLoginTime'],user['archived'],user['orgUnitPath'])
        print("Si está registrado")
        return(True)
    except:
        print("No está registrado")
        return(False)
 


def consultaOrga(unit):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    service = build('admin', 'directory_v1', credentials=creds)
    print("Unidad "+unit)
    #Consulta los usuarios por unidad
    results=service.users().list(customer='my_customer', query='orgUnitPath=/'+unit, viewType='admin_view').execute()
    users=results.get('users',[])   

    if not users:
        print('No  hay usuarios en esta unidad')

    else:
        print('Existen ' +str(len(users)) +' usuarios en la unidad /'+str(unit))
        today=datetime.now()
        fecha=today.strftime("%d%m%Y - %H%M%S")
        print(today)
        r=input('Desea guardarlos en un archivo? y/n:   ')
        
        if r=="y":
            with open('Usuarios en unidad '+str(unit)+' al '+str(fecha)+'.csv','w',newline='',encoding='utf-8') as file:
                filewriter = csv.writer(file,delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)
                filewriter.writerow(['ID Usuario','Nombre','Apellido', 'Last Login', 'Archived', 'orgUnitPath' ])

                print('Usuarios:')
                for user in users:
                    #Imprime los usuarios y genera reporte
                    print(user['id'],user['name']['givenName'],user['name']['familyName'],user['lastLoginTime'],user['archived'],user['orgUnitPath'])
                    filewriter.writerow([user['id'],user['name']['givenName'],user['name']['familyName'],user['lastLoginTime'],user['archived'],user['orgUnitPath']])
        elif r=="n":
            print('Usuarios: ')
            for user in users:
                #Imprime los usuarios y genera reporte
                print(user['id'],user['name']['givenName'],user['name']['familyName'],user['lastLoginTime'],user['archived'],user['orgUnitPath'])

def consulta():
    opcion = int(input("""
    1. Consulta por usuario
    2. Consulta por grupo organizativo

    Ingrese un numero: """))
    if opcion == 1:
        correo=input("""
        
        Ingrese correo de estudiante: """)
        consultaAlumno(correo)

    elif opcion==2:
        unidad=input("""
        Ingrese unidad organizativa: 
        """)
        consultaOrga(unidad)
