from rest_framework import viewsets, generics

from school.models import Student, Course, Enrollment
from school.serializers import (
    StudentSerializer,
    CourseSerializer,
    EnrollmentSerializer,
    ListStudentEnrollmentsSerializer)


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


class ListStudentEnrollments(generics.ListAPIView):
    """Lists student enrollments."""
    serializer_class = ListStudentEnrollmentsSerializer

    def get_queryset(self):
        """Returns queryset with all enrollments of a student."""
        queryset = Enrollment.objects.filter(student_id=self.kwargs['pk'])
        return queryset
