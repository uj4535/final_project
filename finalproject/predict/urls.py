from . import views
from django.urls import path
urlpatterns=[
        path("form", views.form, name="form"),
        path('', views.form, name='form'),
        path('predmodel', views.predmodel, name='predmodel')
]