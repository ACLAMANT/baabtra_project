from django.urls import path
from . import views

urlpatterns = [
    path ('baabtra_css', views.baabtra_css, name='baabtra_css' ),
    path ('courses', views.courses, name='courses' ),
    path ('contactus' , views.contactus, name='contactus'),
]