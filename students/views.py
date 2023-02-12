from flask import request, Response, Blueprint, render_template, url_for, redirect
from .models import Student
from flask_app import db
from . import student_bp


# the reason for hierarchy of templates is to make it more clear where a templates is

# student_bp = Blueprint('student_bp', __name__, template_folder='templates')


@student_bp.route('/')
def index():
    students = Student.query.all()
    return render_template('students/index.html', students=students)


@student_bp.route('/<int:student_id>/')
def student(student_id):
    student = Student.query.get_or_404(student_id)
    return render_template('students/student.html', student=student)


@student_bp.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        age = int(request.form['age'])
        bio = request.form['bio']
        student = Student(firstname=firstname,
                          lastname=lastname,
                          email=email,
                          age=age,
                          bio=bio)
        db.session.add(student)
        db.session.commit()

        return redirect(url_for('student_bp.index'))

    return render_template('students/create.html')


@student_bp.route('/<int:student_id>/edit/', methods=('GET', 'POST'))
def edit(student_id):
    student = Student.query.get_or_404(student_id)

    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        age = int(request.form['age'])
        bio = request.form['bio']

        student.firstname = firstname
        student.lastname = lastname
        student.email = email
        student.age = age
        student.bio = bio

        db.session.add(student)
        db.session.commit()

        return redirect(url_for('student_bp.index'))

    return render_template('students/edit.html', student=student)


@student_bp.post('/<int:student_id>/delete/')
def delete(student_id):
    student = Student.query.get_or_404(student_id)
    db.session.delete(student)
    db.session.commit()
    return redirect(url_for('student_bp.index'))
