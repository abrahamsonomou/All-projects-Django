from django.urls import path
from .views import *

urlpatterns = [

############ Jobforest ################################

    path('',jobforest_home,name='jobforestHome'),
    path('jobforestEmployers/',jobforest_employers,name='jobforestEmployers'),
    path('jobforestEmployersDetails/',jobforest_employersDetails,name='jobforestEmployersDetails'),
    path('jobforestCandidats/',jobforest_candidats,name='jobforestCandidats'),
    path('jobforestCandidatsDetails/',jobforest_candidatsDetails,name='jobforestCandidatsDetails'),
    path('jobforestBlog/',jobforest_blog,name='jobforestBlog'),
    path('jobforestBlogDetails/',jobforest_blogDetails,name='jobforestBlogDetails'),
    path('jobforestListJob/',jobforest_listJob,name='jobforestListJob'),
    path('jobforestListJobDetails/',jobforest_listJobDetails,name='jobforestListJobDetails'),
    
    ################## Profile ##############
    path('jobforestProfile/',jobforest_profile,name='jobforestProfile'),
    path('jobforestResume/',jobforest_resume,name='jobforestResume'),
    path('jobforestCv-manager/',jobforest_cv_manager,name='jobforestCv-manager'),
    path('jobforestJobalerts/',jobforest_jobalerts,name='jobforestJobalerts'),
    path('jobforestAppliedjobs/',jobforest_appliedjobs,name='jobforestAppliedjobs'),
    path('jobforestFavouritejobs/',jobforest_favouritejobs,name='jobforestFavouritejobs'),
    # path('jobforest/',jobforest_,name='jobforest'),
    # path('jobforest/',jobforest_,name='jobforest'),

    ################################ auth ##################
    path('jobforestLogin/',jobforest_login,name='jobforestLogin'),
    path('jobforestRegister/',jobforest_register,name='jobforestRegister'),


    path('jobforestDashboard/',jobforest_dashboard,name='jobforestDashboard'),

############ End Jobforest ################################

]
