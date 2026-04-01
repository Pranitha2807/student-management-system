from django.urls import path
from . import views

urlpatterns = [
    path('', views.grid),  # homepage
    path('carousel/', views.carousel),
    path('table/', views.table),
    path('students/', views.student_view, name='students'),
    path('students/', views.student_list, name='students'),
    path('update/<int:id>/', views.update_student, name='update'),
    path('delete/<int:id>/', views.delete_student, name='delete'),
    path('set-session/', views.set_session),
    path('get-session/', views.get_session),
    path('set-cookie/', views.set_cookie),
    path('get-cookie/', views.get_cookie),
]