import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "enter your database url"
})

ref = db.reference('Students')

data = {
    "9970":
        {
            "name":  "Neel Khot",
            "dept": "Comps B",
            "start_year": "2022",
            "total_attendance": 7,
            "standing": "SE",
            "year": "19",
            "last_attendance-time": "2024-02-08 21:00:00"
        },

    "9974":
        {
            "name":  "Shlok Madve",
            "dept": "Comps B",
            "start_year": "2022",
            "total_attendance": 28,
            "standing": "SE",
            "year": "20",
            "last_attendance_time": "2024-02-08 21:00:00"
        },

    "9987":
        {
            "name":  "Rahel Pereira",
            "dept": "Comps B",
            "start_year": "2022",
            "total_attendance": 15,
            "standing": "SE",
            "year": "19",
            "last_attendance-time": "2024-02-08 21:00:00"
        },

    "10003":
        {
            "name":  "Gauri Waghulade",
            "dept": "Comps B",
            "start_year": "2022",
            "total_attendance": 10,
            "standing": "SE",
            "year": "21",
            "last_attendance-time": "2024-02-08 21:00:00"
        }
}

for key, value in data.items():
    ref.child(key).set(value)
