from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('test.html')  # HTML chứa form và ô lắng nghe

@app.route('/submit', methods=['POST'])
def submit():
    # Lấy dữ liệu từ form
    name = request.form.get('name')
    dob = request.form.get('dob')
    gender = request.form.get('gender')
    months = request.form.get('months')
    pt_info = request.form.get('ptInfo')

    # Trả về phản hồi JSON
    response = {
        "status": "success",
        "message": f"Dữ liệu của {name} đã được gửi lên server.",
        "data": {
            "name": name,
            "dob": dob,
            "gender": gender,
            "months": months,
            "pt_info": pt_info
        }
    }
    return jsonify(response)

@app.route('/update-data', methods=['GET'])
def update_data():
    # Trả về một thông báo giả lập từ server
    message = "Server đã gửi dữ liệu cập nhật mới!"
    return jsonify({"message": message})

if __name__ == '__main__':
    app.run(debug=True)
