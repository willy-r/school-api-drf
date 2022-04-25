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

Clone this repo and go to back-end directory:

```bash
$ git clone https://github.com/willy-r/school-api-drf.git
$ cd school-api-drf/school-backend
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

You must have **Node** installed on your machine.

Define the following envs:

`REACT_APP_BASE_API_URL` - Base API URL to make requests  
`REACT_APP_API_USERNAME` - Your Django admin account username to authenticate on API  
`REACT_APP_API_PASSWORD` - Your Django admin account password to authenticate on API

Clone this repo and go to front-end directory:

```bash
$ git clone https://github.com/willy-r/school-api-drf.git
$ cd school-api-drf/school-frontend
```

Install dependencies:

```bash
$ npm install # npm
$ yarn install # yarn
```

Run development server:

```bash
$ npm start # npm
$ yarn start # yarn
```

Access app:

[`http://localhost:3000`](http://localhost:3000)


## Running locally with docker-compose

> Soon...
