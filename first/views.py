from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from .models import Assignment
from .models import Subject
from .models import Attendance

# Create your views here.

#___________________________________________________________________________________________
# Home Page.
#___________________________________________________________________________________________

def home(request):
	return render(request,'Home.html')

#___________________________________________________________________________________________
# Admin page OR Login page (User can enter email, and password).
#___________________________________________________________________________________________


def admin_page(request):
	return render(request,'admin/Admin_form.html')

#___________________________________________________________________________________________
# Admin Form Check Weiher Username or password Correct Or Not Check Page.
#___________________________________________________________________________________________


def admin_login_real(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        User = auth.authenticate(username=username,password=password)
        if User is not None:
            auth.login(request,User)
            return render(request,'admin/Admin_Dashboard.html')
        else:
            return HttpResponse("<h1> Something Wrong </h1>")
    else:
        return render(request,'admin/Admin_form.html')

#___________________________________________________________________________________________
# Admin Dashboard Page.
#___________________________________________________________________________________________


def dashboard(request):
	return render(request,'admin/Admin_Dashboard.html')

#___________________________________________________________________________________________
# Admin Add Assignment Page.
#___________________________________________________________________________________________


def add_assignment(request):
	return render(request,'admin/Add_Admin_Assignment.html')

#_____________________________________________________________________________________________
# Admin Assignment Data Inserted Saved.
#_____________________________________________________________________________________________


def data_save(request):
	subject_name = request.POST['subject']
	due_date = request.POST['date']
	assignment_title = request.POST['assignment']
	teacher_name = request.POST['teacher']
	submission_date = request.POST['submission']

	assignment_data = Assignment(subject_name=subject_name,due_date=due_date,assignment_title=assignment_title,teacher_name=teacher_name,submission_date=submission_date)
	assignment_data.save()

	return render(request,'admin/Add_Admin_Assignment.html')


#___________________________________________________________________________________________
# Admin Assignments Data Show With The Help Of Table.
#___________________________________________________________________________________________


def table_assignment(request):
	all_data = Assignment.objects.all()
	return render(request,'admin/Table_Assignment.html',{'data':all_data})


#_____________________________________________________________________________________________
# Admin Assignment Data Deleted Page.
#_____________________________________________________________________________________________


def delete(request,id):
	datas = Assignment.objects.get(id=id)
	datas.delete()
	return redirect('/table_assignment')


#_____________________________________________________________________________________________
# Admin Assignment Data Edit Page.
#_____________________________________________________________________________________________


def admin_assignment_edit(request,id):
	datas = Assignment.objects.get(id=id)
	return render(request,'admin/Admin_Assignment_Edit_Update.html',{'data':datas})


#_____________________________________________________________________________________________
# Admin Assignment Data Updated Page.
#_____________________________________________________________________________________________


def admin_assignment_edit_update(request,id):
	id_take = request.POST['id']
	subject_name = request.POST['subject']
	due_date = request.POST['date']
	assignment_title = request.POST['assignment']
	teacher_name = request.POST['teacher']
	submission_date = request.POST['submission']

	assignment_data = Assignment(id=id_take,subject_name=subject_name,due_date=due_date,assignment_title=assignment_title,teacher_name=teacher_name,submission_date=submission_date)
	assignment_data.save()
	return HttpResponse("Success")


#___________________________________________________________________________________________
# Admin Add Subject Page.
#___________________________________________________________________________________________


def add_subject(request):
	return render(request,'admin/Add_Admin_Subject.html')


#___________________________________________________________________________________________
# Admin Subject Data Inserted Saved.
#___________________________________________________________________________________________

def data_save_subject(request):
	subject_name = request.POST['subject']
	due_date = request.POST['date']
	teacher_name = request.POST['teacher']
	description = request.POST['description']

	subject_data = Subject(subject_name=subject_name,due_date=due_date,teacher_name=teacher_name,description=description)
	subject_data.save()
	return render(request,'admin/Add_Admin_Subject.html')

#___________________________________________________________________________________________
# Admin Subjects Data Show With The Help Of Table.
#___________________________________________________________________________________________

def table_subject(request):
	all_data = Subject.objects.all()
	return render(request,'admin/Table_Subject.html',{'data':all_data})


#___________________________________________________________________________________________
# Admin Subject Data Deleted Page.
#___________________________________________________________________________________________

def delete_subject(request,id):
	datas = Subject.objects.get(id=id)
	datas.delete()
	return redirect('/table_subject')

#_____________________________________________________________________________________________
# Admin Attendance Page
#_____________________________________________________________________________________________


def add_attendance(request):
	return render(request,'admin/Add_Admin_Attendance.html')

#_____________________________________________________________________________________________
# Admin Attendance Data Inserted Saved.
#_____________________________________________________________________________________________


def data_save_attendance(request):
	subject_name = request.POST['subject']
	student_name = request.POST['student']
	lecture_title = request.POST['lecture']
	date = request.POST['date']
	description = request.POST['description']

	attendance_data = Attendance(subject_name=subject_name,student_name=student_name,lecture_title=lecture_title,date=date,description=description)
	attendance_data.save()
	return render(request,'admin/Add_Admin_Attendance.html')


#_____________________________________________________________________________________________
# Admin Attendance Data Show With the of Table.
#_____________________________________________________________________________________________


def table_attendance(request):
	all_data = Attendance.objects.all()
	return render(request,'admin/Table_Attendance.html' , {'data':all_data})

#_____________________________________________________________________________________________
# Admin Attendance Data Deleted Page.
#_____________________________________________________________________________________________


def delete_attendance(request,id):
	datas = Attendance.objects.get(id=id)
	datas.delete()
	return redirect('/table_attendance')


#_____________________________________________________________________________________________
# Admin User Page.
#_____________________________________________________________________________________________


def add_user(request):
	return render(request,'admin/Add_Admin_User.html')


#_____________________________________________________________________________________________
# Admin User Data Inserted saved.
#_____________________________________________________________________________________________


def data_save_user(request):
	user_first = request.POST['first']
	user_last = request.POST['last']
	user_id = request.POST['id']
	user_password = request.POST['password']
	user_confirm = request.POST['confirm']
	user_email = request.POST['email']

	user_data = User.objects.create_user(username=user_id,password=user_password,email=user_email,first_name=user_first,last_name=user_last)
	user_data.save()
	return render(request,'admin/Add_Admin_User.html')

#_____________________________________________________________________________________________
# Admin User Data Show With The Help Of Table.
#_____________________________________________________________________________________________

def table_user(request):
	all_data2 = User.objects.all()
	return render(request,'admin/Table_User.html' , {'data':all_data2})


#_____________________________________________________________________________________________
# Admin User Data Deleted Page.
#_____________________________________________________________________________________________


def delete_user(request,id):
	datas = User.objects.get(id=id)
	datas.delete()
	return redirect('/table_user')

def admin_user_edit(request,id):
	datas = User.objects.get(id=id)
	return render(request,'admin/Admin_User_Edit.html',{'data':datas}) 


def admin_user_data_update(request,id):
	id_taken = request.POST['id']
	user_role = request.POST['role']
	user_class = request.POST['class']
	first_name = request.POST['first']
	last_name = request.POST['last']
	login_id = request.POST['login_id']
	password = request.POST['password']

	user_data = User(id=id_taken,user_role=user_role,user_class=user_class,first_name=first_name,last_name=last_name,login_id=login_id,password=password)
	user_data.save()
	return HttpResponse("Success")


#__________________________________________________________________________
# Admin Change Password Page.
#__________________________________________________________________________

def admin_password(request):
	return render(request,'admin/Admin_Change_Password.html')

#__________________________________________________________________________
# Admin Account Mean Add User Page.
#__________________________________________________________________________

def admin_account(request):
	return render(request,'admin/Admin_Account.html')



#============================================================================================
# 									Teacher Area Start
#============================================================================================


def teacher_login(request):
	return render(request,'Teacher_form.html')


def teacher_login_real(request):
	username1 = request.POST['username']
	password1 = request.POST['password']

	data1 = User.objects.all()
	for datas in data1:
		user = datas.login_id
		passw = datas.password

		if user == username1 and passw == password1:
			return render(request,'teacher/Teacher_Dashboard.html')
		else:
			return HttpResponse("Something Wrong")



#============================================================================================
# 									Student Area Start
#============================================================================================


def student_login(request):
	return render(request,'student/Student_form.html')


def student_login_real(request):
	username1 = request.POST['username']
	password1 = request.POST['password']
	user = auth.authenticate(username=username1,password=password1)
	if user is not None:
		auth.login(request,user)
		return render(request,'student/Student_Dashboard.html')
	else:
		return HttpResponse("Something Wrong")




