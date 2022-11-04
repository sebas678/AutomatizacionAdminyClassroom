
from __future__ import print_function
from dataclasses import dataclass
from operator import concat

import os.path
import consultaSistema
from tkinter import filedialog as fd #Libreria para escoger archivo
import xlrd
import csv 


from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/admin.directory.user',
'https://www.googleapis.com/auth/admin.directory.group',
'https://www.googleapis.com/auth/admin.directory.orgunit']

def agregarIndiv(name, familyName, mail, altMail, unitOrgPath):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    service = build('admin', 'directory_v1', credentials=creds)

    if (consultaSistema.consultaAlumno(mail)==False):
        try:
            newUserInfo={
             "name": {
                    "familyName": familyName,
                    "givenName": name
              },
                "password": "primer.password-2023",
                "primaryEmail": mail,
                "changePasswordAtNextLogin": True,
                "orgUnitPath": "/"+unitOrgPath,
                "recoveryEmail": altMail    
            }
            #print("Usuario creado")
            #print(newUserInfo)
            usuario=service.users().insert(body=newUserInfo).execute()
            print("Se registró a: "+name+" "+familyName+" en la unidad /"+unitOrgPath)
        except:
            print("No se pudo registrar a "+mail)
    else:
        print("Ya existe")


def agregarLote(path):
    #creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    #service = build('admin', 'directory_v1', credentials=creds)
    try:
        dataUsuario=xlrd.open_workbook(path)
        hojaData=dataUsuario.sheet_by_index(0)
        try:
            columnas=hojaData.nrows
            print(columnas)
            for i in range (1, columnas):
                nombre=(str(hojaData.cell_value(i,0)))
                apellido=(str(hojaData.cell_value(i,1)))
                correo=(str(hojaData.cell_value(i,2)))
                orgUnit=(str(int(hojaData.cell_value(i,3))))
                recovery=(str(hojaData.cell_value(i,4)))
                agregarIndiv(nombre, apellido, correo, recovery, orgUnit)
        except:
            print("Error en las columnas de información")
    except:
        print("Error en la dirección o tipo de dato")


def agregar():
    opcion = int(input("""
    1. Agregar usuario individual
    2. Agregar desde archivo

    Ingrese un numero: """))
    if opcion == 1:
        nombre=input("Ingrese nombres ")
        apellidos=input("Ingrese apellidos ")
        correo=input("Ingrese correo: ")
        correoAlt=input("Ingrese un correo alternativo ")
        uniOrg=input("Ingrese unidad organizativa a la que pertenece: ")

        agregarIndiv(nombre, apellidos, correo, correoAlt, uniOrg)

    elif opcion==2:
        ruta = fd.askopenfilename()#abre explorador de archivos para elegir ruta
        print(ruta)
        agregarLote(ruta)
