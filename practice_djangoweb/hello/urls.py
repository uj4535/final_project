from hello import views
from django.urls import path
urlpatterns=[
        path("", views.home, name="hello-home"),
        path("form/", views.form, name='form'),
        path('template/', views.template, name='template')
        #path('simpleapi/', views.simpleapi, name='simpleapi')
        ]

