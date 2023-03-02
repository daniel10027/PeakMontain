from django.contrib import admin
from django.urls import path
from django.urls import include, path
from .views import *

urlpatterns = [
    path('',peakList,name="liste"),
    path('peak/detail/<int:pk>/',peakDeatil,name="detail" ),
    path('peak/create/', peakCreate, name="create"),
    path('peak/update/<int:pk>/',peakUpdate,name="update" ),
    path('peak/delete/<int:pk>/',peakDelete,name="delete" ),
    path('peak/getinbox/<slug:lat1>/<slug:long1>/<slug:lat2>/<slug:long2>/<slug:lat3>/<slug:long3>/<slug:lat4>/<slug:long4>/', peakListInZone, name="zone"),
]
