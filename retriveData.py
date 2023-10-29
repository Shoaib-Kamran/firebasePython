import firebase_admin
from firebase_admin import db

# Download Credential File with JSON Extensions From Firebase
cred = firebase_admin.credentials.Certificate('xxxxxxxx.json')
default_app = firebase_admin.initialize_app(cred, {
    'databaseURL': 'firebase database url'
})
ref = db.reference("/")
# Get Data From Firebase Database in JSON Format
print(ref.get())
