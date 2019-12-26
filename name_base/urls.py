from django.urls import path
from . import views
from .views import *
urlpatterns = [

    path('', plist, name='plist'),
    path('inform/<str:slug>/', views.inform, name='inform'),
    path('inform_edit/<str:slug>', views.inform_edit, name='inform_edit'),
    path('personal/', views.personal, name='personal'),
    path('inform_pdf/<str:slug>/', views.inform_pdf, name='inform_pdf'),
   
]