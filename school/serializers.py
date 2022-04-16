from rest_framework import serializers

from school.models import Student, Course, Enrollment


class StudentSerializer(serializers.ModelSerializer):
    """The Student serializer, that translate from JSON to Python, and vice-versa."""
    class Meta:
        model = Student
        fields = ['id', 'name', 'rg', 'cpf', 'birth_date']


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
