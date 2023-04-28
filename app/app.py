from flask import Flask, request, jsonify, render_template
import mysql.connector

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/vaccination-status', methods=['POST'])
def get_vaccination_status():
    data = request.form.to_dict()
    reg_no = data['reg_no']

    db = mysql.connector.connect(
        host='db',
        user='root',
        password='password',
        database='student_vaccination_db'
    )

    cursor = db.cursor()
    cursor.execute(f"SELECT Vaccination_Status FROM Students WHERE RegNo='{reg_no}'")
    result = cursor.fetchone()

    if result:
        return render_template('result.html', vaccination_status=result[0])
    else:
        return render_template('result.html', error='Invalid registration number')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
