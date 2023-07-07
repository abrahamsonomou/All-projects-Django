from django.urls import path

from e_learning.views import studentView
# (
#     studentLogin, studentRegister,
#     studentProfile, studentResetPassword
# )

urlpatterns = [
    path('studentLogin', studentView.studentLogin, name='studentLogin'),
    path('studentRegister', studentView.studentRegister, name='studentRegister'),
    path('student_reset_password', studentView.studentResetPassword, name='student_reset_password'),
    path('studentProfile', studentView.studentProfile, name='studentProfile'),
]

