from rest_framework import viewsets

from school.models import Student, Course, Enrollment
from school.serializers import (
    StudentSerializer, CourseSerializer, EnrollmentSerializer)


class StudentViewSet(viewsets.ModelViewSet):
    """Viewset for students."""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """Viewset for courses."""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class EnrollmentViewSet(viewsets.ModelViewSet):
    """Viewset for enrollments."""
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
