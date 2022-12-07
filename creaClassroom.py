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


def main():
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    service = build('classroom', 'v1', credentials=creds)

    rutaDocumento = fd.askopenfilename()
    
    with open(rutaDocumento,'r') as file:
        cursos= csv.reader(file)
        header=next(cursos)
        if header != None:
            for curso in cursos:
                nombreCurso=(str(curso[0]) + " - "+str(curso[1]))
                seccion=int(curso[2])
                seccionCurso=str(seccion)
                propietario=str(curso[4])
                print(nombreCurso+" "+seccionCurso+" "+propietario)

                # Crea el curso
                course = {
                    'name': nombreCurso,
                    'section': seccionCurso,
                    'ownerId': propietario,
                    'courseState': 'ACTIVE'
                }
                #course = service.courses().create(body=course).execute()
                #print ('Course created: {0} ({1})'.format(course.get('name'), course.get('id')))
