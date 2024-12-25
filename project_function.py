import firebase_admin
from firebase_admin import db, credentials
from firebase_admin import db
from datetime import datetime
import json
import string
import random


cred = credentials.Certificate("json_file.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://iot-gym-ccbc3-default-rtdb.firebaseio.com'
})
def insertData(full_name, dob, gender, train_time, PtInfo, phoneNumber, uid):
    now = datetime.now()
    date_string = now.strftime("%d-%m-%Y")
    # time_string = now.strftime("%H-%M-%S")
    ref = db.reference('/')
    data = {
        'Name':f'{full_name}',
        'Dob':f'{dob}',
        'Gender':f'{gender}',
        'TrainPeriod':f'{train_time}',
        'PtInfo':f'{PtInfo}',
        'Activation_date':f'{date_string}',
        'PhoneNumber': f'{phoneNumber}'
    }
    ref.child(f'{uid}').set(data)
    print("Data pushed successfully")
def deleteData():
    ref = db.reference('/now_UID')
    try:
        ref.delete()
        print("Dữ liệu đã được xóa thành công.")
    except Exception as e:
        print(f"Lỗi khi xóa dữ liệu: {e}")
def check_pass(account, password, admin, admin_pass):
    if account == admin and password == admin_pass:
        return True
    return False
def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string
def check_data():
    ref = db.reference('now_UID')
    data = ref.get()
    return data
#C3CD25E0
def insertTT(uid):
    now = datetime.now()
    date_string = now.strftime("%d-%m-%Y %H:%M:%S")
    ref = db.reference(f'{uid}/Tracking-log')
    data = {
        'TimeStamp':f'{date_string}'
    }
    ref.set(data)

def check_id_exists(id_to_check):
    # Lấy toàn bộ dữ liệu
    ref = db.reference('/')
    data = ref.get()
    print(data)
    # Kiểm tra ID
    if data and id_to_check in data:
        return True
    return False
# print(check_id_exists("C3CD25E0"))