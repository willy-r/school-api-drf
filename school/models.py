from django.db import models


class Student(models.Model):
    """Represents a Student in the database."""
    name = models.CharField(max_length=30)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    birth_date = models.DateField()

    def __str__(self) -> str:
        return self.name.title()


class Course(models.Model):
    """Represents a Course in the database."""
    BASIC = 'B'
    INTERMEDIATE = 'I'
    ADVANCED = 'A'
    NIVEL = (
        (BASIC, 'Basic'),
        (INTERMEDIATE, 'Intermediate'),
        (ADVANCED, 'Advanced'),
    )

    course_code = models.CharField(max_length=10)
    description = models.CharField(max_length=100)
    level = models.CharField(
        max_length=1, 
        choices=NIVEL,
        blank=False,
        null=False,
        default=BASIC)

    class Meta:
        verbose_name_plural = 'courses'
    
    def __str__(self) -> str:
        if len(self.description) > 50:
            return self.description[:50]
        
        return self.description
