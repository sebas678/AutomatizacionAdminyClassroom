#En este programa se solicita la instrucción a realizar
#  Consultar alumno en sistema
#  Agregar alumno a sistema
#  Consultar Classrooms de alumno
#  Agregar alumno a classroom
#  Consultar classroom existentes
#  Crear classrooms
from __future__ import print_function

import consultaSistema

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/admin.directory.user',
'https://www.googleapis.com/auth/admin.directory.group',
'https://www.googleapis.com/auth/admin.directory.orgunit']


creds = None
#Corrobora la existencia del archivo token.json
if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
#Si no existen las credenciales hace proceso de Login
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
    #Guarda las credenciales para la próxima
    with open('token.json', 'w') as token:
        token.write(creds.to_json())

service = build('admin', 'directory_v1', credentials=creds)

opcion= int(input("""
Ingrese el numero correspondiente a la operación:

1. Consultar alumno
2. Agregar alumno a sistema
3. Consultar Classroom de alumno
4. Agregar alumno a Classroom
5. Consultar classroom existentes
6. Crear classroom

Ingrese un numero: """))
if opcion == 1:
    #Consulta alumno en sistema
    consultaSistema.consulta()
'''
elif opcion == 2:
    #Agrgra alumno a sisteme
elif opcion == 3:
    #consulta classroom
elif opcion == 4: 
    #Agrega a classroom
elif opcion == 5: 
    #Consulta classrooms existentes
elif opcion == 6:
    #Crea Classroom
    '''
