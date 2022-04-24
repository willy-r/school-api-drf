from django.db import models


class Student(models.Model):
    """Represents a Student in the database."""
    name = models.CharField(max_length=30)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    birth_date = models.DateField()
    cellphone = models.CharField(max_length=11, default='')

    def __str__(self) -> str:
        return self.name.title()


class Course(models.Model):
    """Represents a Course in the database."""
    BASIC = 'B'
    INTERMEDIATE = 'I'
    ADVANCED = 'A'
    LEVELS = (
        (BASIC, 'Basic'),
        (INTERMEDIATE, 'Intermediate'),
        (ADVANCED, 'Advanced'),
    )

    course_code = models.CharField(max_length=10)
    description = models.CharField(max_length=100)
    level = models.CharField(
        max_length=1, 
        choices=LEVELS,
        blank=False,
        null=False,
        default=BASIC)
    
    def __str__(self) -> str:
        if len(self.description) > 50:
            return self.description[:50]
        
        return self.description


class Enrollment(models.Model):
    """Student enrolls Course."""
    MORNING = 'M'
    AFTERNOON = 'A'
    NIGHTLY = 'N'
    PERIODS = (
        (MORNING, 'Morning'),
        (AFTERNOON, 'Afternoon'),
        (NIGHTLY, 'Nightly'),
    )

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    period = models.CharField(
        max_length=1, 
        choices=PERIODS,
        blank=False,
        null=False,
        default=MORNING)
