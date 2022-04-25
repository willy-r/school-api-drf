"""Populates development database with some data."""

import os
import sys
import random

import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from faker import Faker
from validate_docbr import CPF

from school.models import  Student, Course


def create_students(students: int) -> None:
    """Populates the database with students."""
    fake = Faker('pt_BR')
    Faker.seed(10)
    
    for _ in range(students):
        cpf = CPF()
        name = fake.name()
        rg = '{}{}{}{}'.format(
            random.randrange(10, 99),
            random.randrange(100, 999),
            random.randrange(100, 999),
            random.randrange(0, 9)) 
        cpf = cpf.generate()
        birth_date = fake.date_between(start_date='-18y', end_date='today')
        
        student = Student(name=name, rg=rg, cpf=cpf, birth_date=birth_date)
        student.save()


def create_courses(courses: int) -> None:
    Faker.seed(10)

    for _ in range(courses):
        course_code = '{}{}-{}'.format(
            random.choice('ABCDEF'),
            random.randrange(10, 99),
            random.randrange(1, 9))
        course_descriptions = [
            'Python Fundamentos',
            'Python intermediário',
            'Python Avançado',
            'Python para Data Science',
            'Python/React'
        ]
        description = random.choice(course_descriptions)
        course_descriptions.remove(description)
        level = random.choice('BIA')
        
        course = Course(course_code=course_code, description=description, level=level)
        course.save()


if __name__ ==  '__main__':
    try:
        students, courses = sys.argv[1:3]
        create_students(int(students))
        create_courses(int(courses))
    except Exception:
        print(f'usage: python {sys.argv[0]} [students] [courses]')
