from django.urls import path
from core.views.serviceViews import (
    ServiceList, ServiceListDetail,
    services
)

urlpatterns = [
    path('',services,name='services'),

        # services 
    path(r'api/Services/',ServiceList.as_view(),name='Services/'),
    path(r'api/(?P<pk>[0-9]+)/$', ServiceListDetail.as_view(),name='Servicedetails/'), 
    

]
