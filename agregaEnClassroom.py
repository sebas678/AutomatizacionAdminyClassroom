from __future__ import print_function
from datetime import datetime


import csv
from tkinter import filedialog as fd #Libreria para escoger archivo


import os.path
from unicodedata import name

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient import errors
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/admin.directory.user',
'https://www.googleapis.com/auth/admin.directory.group',
'https://www.googleapis.com/auth/admin.directory.orgunit',
'https://www.googleapis.com/auth/classroom.courses']


def agregaIndiv(correo, cursoId):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    service = build('classroom', 'v1', credentials=creds)
    student={
        'userId':correo
    }
    try:
        student = service.courses().students().create(courseId=cursoId,body=student).execute()
        print("Usuario asignado")
        return True
    
    except errors.HttpError as error:
        print("Ya estas asignado en este curso")

def agregaLoteSelec(rutaCorreo, rutaCursos):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    service = build('classroom', 'v1', credentials=creds)
    with open(rutaCorreo,'r') as file:
        correos=csv.reader(file)
        for correo in correos:
            print(correo[0])
            

def main():    
    opcion= int(input("""
    Seleccione el numero de operación:

    1. Agregar usuario indiviudal
    2. Agregar usuarios por lote a definir
    3. Agregar usuarios en lote definido
    
    Ingrese acá un numero:   """))

    if opcion == 1:
        mail=input("Ingrese un correo valido en el sistema:  ")
        idCourse=input("Ingrese un Id de curso valido:  ")
        agregaIndiv(mail, idCourse)

    elif opcion ==2:
        print("Selecciona archivo con correos")
        rutaMail = fd.askopenfilename()
        #print("Selecciona archivo con cursos")
        #rutaCourse= fd.askopenfilename()

        agregaLoteSelec(rutaMail,"")