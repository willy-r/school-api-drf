from rest_framework import routers

from school import views

router = routers.DefaultRouter()

# All routers with CRUD.
router.register('students', views.StudentViewSet, basename='Students')
router.register('courses', views.CourseViewSet, basename='Courses')
router.register('enrollments', views.EnrollmentViewSet, basename='Enrollments')
