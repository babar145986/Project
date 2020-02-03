from django.urls import path
from . import views

urlpatterns = [

	#__________________________________________________________________________
	# Admin Home Page.
	path('',views.home,name='home'),
	#__________________________________________________________________________


	#__________________________________________________________________________
	# Admin Login Page
	path('admin_page/',views.admin_page,name='admin'),
	#__________________________________________________________________________


	#__________________________________________________________________________
	# Admin Login Page User Check For Authenticating Username,Password.
	path('admin_login_real/',views.admin_login_real,name='admin_login_real'),
	#__________________________________________________________________________


	#__________________________________________________________________________
	# Admin Dashboard Page.
	path('dashboard/',views.dashboard,name='dashboard'),
	#__________________________________________________________________________


	#__________________________________________________________________________
	# Admin Add Assignment Page.
	path('add_assignment/',views.add_assignment,name='add_assignment'),
	#__________________________________________________________________________


	#__________________________________________________________________________
	# Admin Add Assignment Data Saved Page.
	path('data_save/',views.data_save,name='data_save'),
	#__________________________________________________________________________


	#__________________________________________________________________________
	# Admin Add Assignment Data Show In Table Page.
	path('table_assignment/',views.table_assignment,name='table_assignment'),
	#__________________________________________________________________________


	#_________________________________________________________________________
	# Admin Assignment Data Deleted Page.
	path('delete/<int:id>',views.delete,name='delete'),
	#_________________________________________________________________________


	#__________________________________________________________________________
	# Admin Assignment Data Edit For Update.
	path('admin_assignment_edit/<int:id>',views.admin_assignment_edit,name='admin_assignment_edit'),
	#__________________________________________________________________________


	#__________________________________________________________________________
	# Admin Assignment Data Updated Page.
	path('admin_assignment_edit_update/<int:id>',views.admin_assignment_edit_update,name='admin_assignment_edit_update'),
	#__________________________________________________________________________


	#__________________________________________________________________________
	# Admin Add Subject Page.
	path('add_subject/',views.add_subject,name='add_subject'),
	#__________________________________________________________________________


	#__________________________________________________________________________
	# Admin Add Subject Data Saved Page.
	path('data_save_subject/',views.data_save_subject,name='data_save_subject'),
	#__________________________________________________________________________

	
	#__________________________________________________________________________
	# Admin Add Subject Data Show Page.
	path('table_subject/',views.table_subject,name='table_subject'),
	#__________________________________________________________________________


	#__________________________________________________________________________
	# Admin Subject Data Deleted Page.
	path('delete_subject/<int:id>',views.delete_subject,name='delete_subject'),
	#__________________________________________________________________________


	#__________________________________________________________________________
	# Admin Add Attendance Page.
	path('add_attendance/',views.add_attendance,name='add_attendance'),
	#__________________________________________________________________________


	#__________________________________________________________________________
	# Admin Add Attendance Data Saved Page.
	path('data_save_attendance/',views.data_save_attendance,name='data_save_attendance'),
	#__________________________________________________________________________


	#__________________________________________________________________________
	# Admin Add Attendance Data Show Page.
	path('table_attendance/',views.table_attendance,name='table_attendance'),
	#__________________________________________________________________________


	#__________________________________________________________________________
	# Admin Attendance Data Deleted Page.
	path('delete_attendance/<int:id>',views.delete_attendance,name='delete_attendance'),
	#__________________________________________________________________________


	#__________________________________________________________________________
	# Admin Add User Page.
	path('add_user/',views.add_user,name='add_user'),
	#__________________________________________________________________________


	#__________________________________________________________________________
	# Admn Add User Data Saved Page.
	path('data_save_user/',views.data_save_user,name='data_save_user'),
	#__________________________________________________________________________


	#__________________________________________________________________________
	# Admin Add User Data Show Page.
	path('table_user/',views.table_user,name='table_user'),
	#__________________________________________________________________________


	#__________________________________________________________________________
	# Admin User Data Deleted.
	path('delete_user/<int:id>',views.delete_user,name='delete_user'),
	#__________________________________________________________________________


	#__________________________________________________________________________
	# Admin Change Password Page.
	path('admin_password/',views.admin_password,name='admin_password'),
	#__________________________________________________________________________


	#__________________________________________________________________________
	# Admin Account Page Where User Want To Add User And Change Password.
	path('admin_account/',views.admin_account,name='admin_account'),
	#__________________________________________________________________________


	#======================== Delete Admin Table Data Pages ==================================

	path('admin_user_edit/<int:id>',views.admin_user_edit,name='admin_user_edit'),

	path('admin_user_data_update/<int:id>',views.admin_user_data_update,name='admin_user_data_update'),

	#=====================================================================================


	#==========================================================================================
	# 								Teacher Area Start
	#==========================================================================================


	#__________________________________________________________________________
	# Teacher Account Page.
	path('teacher_login/',views.teacher_login,name='teacher_login'),
	#__________________________________________________________________________


	path('teacher_login_real/',views.teacher_login_real,name='teacher_login_real'),


	#==========================================================================================
	# 							Student Area Start
	#==========================================================================================


	#__________________________________________________________________________
	# Teacher Account Page.
	path('student_login/',views.student_login,name='student_login'),
	#__________________________________________________________________________


	path('student_login_real/',views.student_login_real,name='student_login_real'),

]
