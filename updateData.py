import firebase_admin
from firebase_admin import db

# Download Credential File with JSON Extensions From Firebase
cred = firebase_admin.credentials.Certificate('xxxxxxxxxx.json')
default_app = firebase_admin.initialize_app(cred, {
    'databaseURL': 'firebase database url'
})
ref = db.reference("/")
# Update Data Into Firebase Database in JSON Format
num = 5
ref.update({'Best_Sellers': f'{num}'})
