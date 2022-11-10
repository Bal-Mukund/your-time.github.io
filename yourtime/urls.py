from django.urls import path
from . import views

urlpatterns = [
    path("",views.cr_time, name="cr_time")
]