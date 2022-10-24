
from __future__ import print_function

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
        results=service.users().get(userKey=mail).execute()
        print("Si está registrado")
    except:
        print("No está registrado")
 


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
        print('Usuarios:')
        for user in users:
            #Imprime los usuarios y genera reporte
            print(user['id'],user['name']['fullName'],user['lastLoginTime'])


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
        
        Ingrese unidad organizativa: """)
        consultaOrga(unidad)
