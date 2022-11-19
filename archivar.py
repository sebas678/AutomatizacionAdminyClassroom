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
                cursoId=curso[0]
                singleCourse=service.courses().get(id=cursoId).execute()
                singleCourse['courseState']='ARCHIVED'
                singleCourse=service.courses().update(id=cursoId,body=singleCourse).execute()
                print('Curso archivado - '+ curso[0] )


'''
    for course in courses:
        print(course['name']+' - '+course['id'])
        courseId=str(course['id'])
        singleCourse=service.courses().get(id=courseId).execute()
        #print(type(singleCourse))
        #print(singleCourse)
        singleCourse['courseState']='DECLINED'
        singleCourse=service.courses().update(id=courseId,body=singleCourse).execute()
'''