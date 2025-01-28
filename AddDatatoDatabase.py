import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://sjs-database-93f73-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {

    "1":
        {
            "name": "Abel Girma",
            "starting_year": 2022,
            "total_attendance": 0,
            "last_attendance_time": "2022-12-11 00:54:34",
            "Major": "Student"
        },
    "2":
        {
            "name": "Nahom tewdros",
            "starting_year": 2018,
            "total_attendance": 0,
            "last_attendance_time": "2022-12-11 00:54:34",
            "Major": "Student"
        },
    "3":
        {
            "name": "Eyuel",
            "starting_year": 2018,
            "total_attendance": 0,
            "last_attendance_time": "2022-12-11 00:54:34",
            "Major": "Student"
        },
    "4":
        {
            "name": "Biruk temesgen",
            "starting_year": 2018,
            "total_attendance": 0,
            "last_attendance_time": "2022-12-11 00:54:34",
            "Major": "Student"
        },
    "5":
        {
            "name": "Teacher Dawit",
            "starting_year": 2018,
            "total_attendance": 0,
            "last_attendance_time": "2022-12-11 00:54:34",
            "Major": "Teacher"
        },
    "5":
        {
            "name": "Abemelek ermias",
            "starting_year": 2018,
            "total_attendance": 0,
            "last_attendance_time": "2022-12-11 00:54:34",
            "Major": "Student"
        }
}
for key, value in data.items():
    ref.child(key).set(value)