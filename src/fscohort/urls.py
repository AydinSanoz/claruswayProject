from django.urls import path
from .views import home_view, main_view, student_list

urlpatterns = [
    path('home/', home_view, name='home'),
    path('main/', main_view, name='main'),
    path('student/', student_list, name = 'student')
]