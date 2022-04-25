import status
from rest_framework import viewsets, generics
from rest_framework.response import Response

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

    def create(self, request):
        """Creates a new course, defining Location header."""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()

            new_course_id = serializer.data['id']
            response = Response(serializer.data, status=status.HTTP_201_CREATED)
            response['Location'] = f'{request.build_absolute_uri()}{new_course_id}'
            return response


class EnrollmentViewSet(viewsets.ModelViewSet):
    """Viewset for enrollments."""
    queryset = Enrollment.objects.all().order_by('id')
    serializer_class = serializers.EnrollmentSerializer
    http_method_names = ['get', 'post', 'put', 'patch']


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
