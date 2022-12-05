from django.urls import path
from .import views
urlpatterns = [
    path('student/', views.student.as_view())

]
