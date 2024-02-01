import os
import firebase_admin
from firebase_admin import credentials

# Get the directory of the current script (firebase_init.py)
current_directory = os.path.dirname(os.path.realpath(__file__))

# Construct the path to the Firebase credentials JSON file
json_file_path = os.path.join(current_directory, 'skimi-3e278-firebase-adminsdk-l2l8g-157721ceab.json')

# Get the absolute path
absolute_path = os.path.abspath(json_file_path)

# Initialize Firebase
cred = credentials.Certificate(absolute_path)
firebase_admin.initialize_app(cred, {'storageBucket': 'skimi-3e278.appspot.com'})
