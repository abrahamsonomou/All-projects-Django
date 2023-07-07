from django.urls import path
from .views import *

urlpatterns = [
    path('',formation,name='formation'),
    path(r'teacher/',TeacherList.as_view(),name='teacher/'),
    path(r'api/(?P<pk>[0-9]+)/$', TeacherListDetail.as_view(),name='teacherdetails/'),
    
    path(r'api/students/',StudentList.as_view(),name='students/'),
    path(r'api/(?P<pk>[0-9]+)/$', StudentListDetail.as_view(),name='studentdetails/'),
    
    path(r'api/competences/',CompetenceList.as_view(),name='competences/'),
    path(r'api/(?P<pk>[0-9]+)/$', CompetenceListDetail.as_view(),name='competencedetails/'),
    
    path(r'api/CourseCategorys/',CourseCategoryList.as_view(),name='CourseCategorys/'),
    path(r'api/(?P<pk>[0-9]+)/$', CourseCategoryListDetail.as_view(),name='CourseCategorydetails/'),
    
    path(r'api/cours/',CoursList.as_view(),name='cours/'),
    path(r'api/(?P<pk>[0-9]+)/$', CoursListDetail.as_view(),name='Coursdetails/'),
]
