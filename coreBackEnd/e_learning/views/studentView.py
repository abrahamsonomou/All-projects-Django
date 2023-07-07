from django.shortcuts import render,redirect

def studentLogin(request):
    return render(request,'auth/student-login.html')

def studentRegister(request):
    return render(request,'auth/student-register.html')

def studentResetPassword(request):
    return render(request,'auth/Student_reset_password.html')

def studentProfile(request):
    return render(request,'students/student-dashboard.html')