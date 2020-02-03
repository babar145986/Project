from django.db import models

# Create your models here.

# Admin Add Assignment Model.

class Assignment(models.Model):
	subject_name = models.CharField(max_length=100)
	due_date = models.CharField(max_length=100)
	assignment_title = models.CharField(max_length=100)
	teacher_name = models.CharField(max_length=100)
	submission_date = models.CharField(max_length=100)


# Admin Add Subject Model.

class Subject(models.Model):
	subject_name = models.CharField(max_length=100)
	due_date = models.CharField(max_length=100)
	teacher_name = models.CharField(max_length=100)
	description = models.CharField(max_length=100)

# Admin Add Attendance Model.

class Attendance(models.Model):
	subject_name = models.CharField(max_length=100)
	student_name = models.CharField(max_length=100)
	lecture_title = models.CharField(max_length=100)
	date = models.CharField(max_length=100)
	description = models.CharField(max_length=100)

# Admin Add User Model.

class User(models.Model):
	user_role = models.CharField(max_length=100)
	user_class = models.CharField(max_length=100)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	login_id = models.CharField(max_length=100)
	password = models.CharField(max_length=100)





