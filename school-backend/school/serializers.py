from rest_framework import serializers

from school.models import Student, Course, Enrollment


class StudentSerializer(serializers.ModelSerializer):
    """The Student serializer, that translate from JSON to Python, and vice-versa."""
    class Meta:
        model = Student
        exclude = ['cellphone']


class CourseSerializer(serializers.ModelSerializer):
    """The Course serializer, that translate from JSON to Python, and vice-versa."""
    class Meta:
        model = Course
        fields = '__all__'


class EnrollmentSerializer(serializers.ModelSerializer):
    """The Enrollment serializer, that translate from JSON to Python, and vice-versa."""
    class Meta:
        model = Enrollment
        fields = '__all__'


class ListStudentEnrollmentsSerializer(serializers.ModelSerializer):
    """Enrollments of a student serializer, translate from JSON to Python, and vice-versa."""
    course_description = serializers.ReadOnlyField(source='course.description')
    period = serializers.SerializerMethodField()

    class Meta:
        model = Enrollment
        fields = ['course_description', 'period']
    
    def get_period(self, obj):
        return obj.get_period_display()


class ListCourseStudentsSerializer(serializers.ModelSerializer):
    """Students of a course serializer, translate from JSON to Python, and vice-versa."""
    student_name = serializers.ReadOnlyField(source='student.name')

    class Meta:
        model = Enrollment
        fields = ['student_name']


class StudentSerializerV2(serializers.ModelSerializer):
    """The Student serializer but for API version 2."""
    class Meta:
        model = Student
        fields = '__all__'
