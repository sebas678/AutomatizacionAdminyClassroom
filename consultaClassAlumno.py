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

def consultaAlumno():
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    service = build('classroom', 'v1', credentials=creds)
    results = service.courses().list(courseStates='ACTIVE').execute()
    courses = results.get('courses', [])