from __future__ import print_function
from datetime import datetime
import csv

import os.path
from unicodedata import name

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/admin.directory.user',
'https://www.googleapis.com/auth/admin.directory.group',
'https://www.googleapis.com/auth/admin.directory.orgunit',
'https://www.googleapis.com/auth/classroom.courses']

def consultaActivo():
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    service = build('classroom', 'v1', credentials=creds)
    results = service.courses().list(courseStates='ACTIVE').execute()
    courses = results.get('courses', [])

    if not courses:
        print('No hay cursos.')
        return

    print('Existen ' +str(len(courses)) +' cursos:')
    today=datetime.now()
    fecha=today.strftime("%d%m%Y%H%M%S")
    print(today)
    r=input('Desea guardarlos en un archivo? y/n:   ')

    if r=="y":
        with open('cursos al '+str(fecha)+'.csv','w',newline='',encoding='utf-8') as file:
            filewriter = csv.writer(file,delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)
            filewriter.writerow(['ID de curso','Curso','Sección', 'Id Propietario'])
            for course in courses:
                try:
                    seccionCurso=course['section']
                    print(course['id']+' - '+seccionCurso+' - '+course['name'])
                except:
                    seccionCurso="N/E"
                    print(course['id']+' - '+seccionCurso+' - '+course['name'])

                filewriter.writerow([course['id'],course['name'],seccionCurso,course['ownerId']])
    else:
        for course in courses:
                try:
                    seccionCurso=course['section']
                    print(course['id']+' - '+seccionCurso+' - '+course['name'])
                except:
                    seccionCurso="N/E"
                    print(course['id']+' - '+seccionCurso+' - '+course['name'])