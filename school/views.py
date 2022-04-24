from rest_framework import viewsets, generics

from school.models import Student, Course, Enrollment
from school import serializers


class StudentViewSet(viewsets.ModelViewSet):
    """Viewset for students."""
    queryset = Student.objects.all().order_by('id')
    
    def get_serializer_class(self):
        """Defines serializer class based on API version."""
        if self.request.version == 'v2':
            return serializers.StudentSerializerV2
        
        return serializers.StudentSerializer

class CourseViewSet(viewsets.ModelViewSet):
    """Viewset for courses."""
    queryset = Course.objects.all().order_by('id')
    serializer_class = serializers.CourseSerializer


class EnrollmentViewSet(viewsets.ModelViewSet):
    """Viewset for enrollments."""
    queryset = Enrollment.objects.all().order_by('id')
    serializer_class = serializers.EnrollmentSerializer


class ListStudentEnrollments(generics.ListAPIView):
    """Lists student enrollments."""
    serializer_class = serializers.ListStudentEnrollmentsSerializer

    def get_queryset(self):
        """Returns queryset with all enrollments of a student."""
        queryset = Enrollment.objects.filter(
            student_id=self.kwargs['pk']).order_by('id')
        return queryset


class ListCourseStudents(generics.ListAPIView):
    """Lists all students of a course."""
    serializer_class = serializers.ListCourseStudentsSerializer

    def get_queryset(self):
        """Returns queryset with all students of a course."""
        queryset = Enrollment.objects.filter(
            course_id=self.kwargs['pk']).order_by('id')
        return queryset
