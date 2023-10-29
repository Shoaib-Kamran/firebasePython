import firebase_admin
from firebase_admin import db

# Download Credential File with JSON Extensions From Firebase
cred = firebase_admin.credentials.Certificate('xxxxxxxxx.json')
default_app = firebase_admin.initialize_app(cred, {
    'databaseURL': 'firebase database url'
})

ref = db.reference("/")
# Insert Data Into Firebase Database in JSON Format
ref.set({"Best_Sellers": -1})
# ref.set({
#     "Books":
#         {
#             "Best_Sellers": -1
#         }
# })
