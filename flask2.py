from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:sainaidu%40799@localhost/employees'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"
    
    
@app.route('/', methods=['GET'])
def index():
    return render_template('index2.html')

# Route to insert values into the Student table
@app.route('/add_student', methods=['POST'])
def add_student():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']

        new_student = Student(username=username, email=email)
        db.session.add(new_student)
        db.session.commit()

        return jsonify({'message': 'Student added successfully'})

# Route to get all students in JSON format
@app.route('/get_students', methods=['GET'])
def get_students():
    students = Student.query.all()
    student_list = [{'id': student.id, 'username': student.username, 'email': student.email} for student in students]
    return jsonify({'students': student_list})

if __name__ == '__main__':
    app.run(debug=True)