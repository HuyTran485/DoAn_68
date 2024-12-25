from flask import Flask, render_template, Response, request, jsonify, redirect, url_for, session, make_response
import time
from datetime import datetime
from project_function import insertData, check_pass, generate_random_string, check_data, deleteData, check_id_exists
import threading
app = Flask(__name__)

#-----------------------------Web-----------------------------------------------
@app.route('/', methods=['POST', 'GET'])
def sign_in():
    global random_id
    error = None
    if request.method == 'POST':
        account = request.form['account']
        password = request.form['password']
        if check_pass(account, password, "Admin", "123456"):
            random_id = generate_random_string(40)
            return redirect(url_for('final_check', account= 'admin', random_pin= random_id))
        else:
            error = 'Invalid room-id or password. Please try again!'
    return render_template('login_page.html', error=error)
@app.route(f'/<account>/<random_pin>', methods=['POST', 'GET'])
def final_check(account, random_pin):
    if request.method == 'POST':
        if request.method == 'POST':
            full_name = request.form['name']
            dob= request.form['dob']
            gender = request.form['gender']
            train_time = request.form['months']
            PtInfo = request.form['ptInfo']
            uid = request.form['flaskData']
            print(full_name, dob, gender, train_time, PtInfo, uid)
    if account == "admin" and random_pin == random_id:
        return render_template("main_page.html")
@app.route('/get-data', methods=['GET'])
def get_data():
    data = check_data()
    if data:
        return jsonify({'status': 'success', 'data': data})
    else:
        return jsonify({'status': 'error', 'message': 'No data found'})

@app.route('/submit-data', methods=['POST'])
def submit_data():
    try:
        # Nhận dữ liệu JSON từ JavaScript
        data = request.get_json()
        # Kiểm tra hoặc xử lý dữ liệu
        # print("Dữ liệu nhận được:", data["name"], data['dob'], data['gender'], data['months'], data['ptInfo'], data['uid'])
        insertData(data["name"], data['dob'], data['gender'], data['months'], data['ptInfo'], data['phoneNumber'], data['uid'])
        #deleteData()
        # Phản hồi lại thành công
        return jsonify({'status': 'success', 'message': 'Dữ liệu đã được nhận'})
    except Exception as e:
        # Phản hồi nếu có lỗi xảy ra
        return jsonify({'status': 'error', 'message': str(e)}), 500
@app.route('/check_uid', methods=['POST','GET'])
def check_uid():
    error = None
    if request.method == 'POST':
        uid = request.form['uid']
        if check_id_exists(uid):
            return redirect(url_for('schedule'))
        else:
            error = 'Uid was not exist. Please try again or sign in at registration counter!'
    return render_template('training_sign.html', error=error)
@app.route('/schedule')
def schedule():
    return render_template('test.html')
#--------------------------------------End------------------------------------------
if __name__ == "__main__":
    app.run()