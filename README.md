# School API - Django Rest Framework

A school REST API made with Django Rest Framework and being consumed by a React front-end app.


## Endpoints

CRUD for Student entity: `/students`  
CRUD for Course entity: `/courses`  
CRUD for Enrollment entity: `/enrollments`

### Special endpoints

| Method | Route | Description |
| ------ | ----- | ----------- |
| **GET** | `/students/{id}/enrollments` | Gets all enrollments of a student by {id} |
| **GET** | `/courses/{id}/enrollments` | Gets all enrollments of a course by {id} |


## Running back-end locally

You need to have **Python 3.7.4+**

Define the following envs:

`SECRET_KEY` - The SECRET KEY for your Django project

Clone this repo and go to project root directory:

```bash
$ git clone https://github.com/willy-r/school-api-drf.git
$ cd school-api-drf
```

Create virtual enviroment and activate it:

```bash
$ python -m venv venv
$ source venv/bin/activate
```

Install dependencies:

```bash
$ (venv) pip install -r requirements.txt
```

Migrate database, create superuser and start server:

```bash
$ (venv) python manage.py migrate
$ (venv) python manage.py createsuperuser
$ ...
$ (venv) python manage.py runserver
```

Access API:

[`http://localhost:8000`](http://localhost:8000)


## Running front-end locally

> Soon...
