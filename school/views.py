from rest_framework import viewsets

from school.models import Student, Course
from school.serializers import StudentSerializer, CourseSerializer


class StudentViewSet(viewsets.ModelViewSet):
    """Displays all students."""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """Displays all available courses."""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
