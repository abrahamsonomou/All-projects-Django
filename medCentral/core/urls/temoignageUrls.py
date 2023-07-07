from django.urls import path
from core.views.temoignageViews import (
    temoignage, TemoignageList, TemoignageListDetail
)

urlpatterns = [
    path('',temoignage,name='temoignage'),

        # Temoignages 
    path(r'api/temoignages/',TemoignageList.as_view(),name='temoignages/'),
    path(r'api/(?P<pk>[0-9]+)/$', TemoignageListDetail.as_view(),name='temoignagedetails/'), 
    

]
