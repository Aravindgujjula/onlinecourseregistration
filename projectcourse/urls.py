"""projectcourse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from appcourse import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('admin_login/', views.admin_login, name="admin_login"),
    path('', views.admin_login, name="admin_login"),
    path('admin_login_check/', views.admin_login_check, name="admin_login_check"),
    path('schedule_class/', views.schedule_class, name="schedule_class"),
    path('save_class/', views.save_class, name="save_class"),
    path('View_all/',views.View_all,name = "View_all"),
    path('update/',views.update,name = "update"),
    path('update_course/',views.update_course,name = "update_course"),
    path('delete/', views.delete, name="delete"),
    #path('show_update/',views.show_update,name = "show_update"),

    path('main',views.main,name = "main"),
    path('course/',views.course,name = "course"),
    path('register/',views.register,name = "register"),
    path('save_reg/',views.save_reg,name = "save_reg"),
    path('login/',views.login,name = "login"),
    path('student_login_check/',views.student_login_check,name = "student_login_check"),

    path('enroll/',views.enroll,name = "enroll"),
    path('viewenroll/',views.viewenroll,name = "viewenroll"),
    #path('save_enroll/',views.save_enroll,name = "save_enroll"),

]

