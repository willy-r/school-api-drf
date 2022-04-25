"""setup URL Configuration

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
from django.urls import path, include

from rest_framework import routers

from school import views

router = routers.DefaultRouter()

# All routers with CRUD.
router.register('students', views.StudentViewSet, basename='Students')
router.register('courses', views.CourseViewSet, basename='Courses')
router.register('enrollments', views.EnrollmentViewSet, basename='Enrollments')

urlpatterns = [
    # API
    path('', include(router.urls)),
    path('students/<int:pk>/enrollments', views.ListStudentEnrollments.as_view()),
    path('courses/<int:pk>/enrollments', views.ListCourseStudents.as_view()),

    # Django admin.
    path('admin/', admin.site.urls),
]
