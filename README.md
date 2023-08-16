# Django_starter #

## 1- Introduction

This project was born for the creation of a software skeleton that serves for the development of projects based on Django.

The main idea is to save work when developing a project, focusing on the development itself, not on the preparations.

For this we have developed this file in python containing all those instructions, software structures and importing the basic libraries necessary for the creation of a project in Django.

## 2- Installation

There are 2 ways to install this project on your computer:

### Way 1. Clone this repository in your development environment.

````bash
git clone https://github.com/iasoloteravision/Django_starter.git
````


Once the repository has been cloned, we are going to the folder where project is located

````bash
cd [project folder]
````

The next step is to generate the migrations so that the libraries and functionalities of the project take effect.

````python
python3 manage.py makemigrations
````

Once the migrations are assembled, we have to transfer them to our development environment.

````python
python3 manage.py migrate
````
Although it is not mandatory, it is always good to create a super user for project administration.

````python
python3 manage.py createsuperuser
````

After answering the questions for the superuser, we are ready for the project to run in all its dimensions.

````python
python3 manage.py runserver
````

Our project is running without problem, we can see it at http://127.0.0.1:8000/ as home page (page that we can later modify depending on the project)

### Way 2. Run my_django_starter.py

1.- Open my_django_starter.py in your preferred editor (I opened it in VSC).

You can change the folder, project name, APPS to use and more configurations between line 16 to 23 to personalize your project. `Don´t forget to save it!`

2.- Run the file with:
````python
python3 my_django_starter.py
````

If you look at your directory tree, the project has already been created and you have the basics and functionality of a complete Django project.

3.- The next step is to generate the migrations so that the libraries and functionalities of the project take effect.

````python
python3 manage.py makemigrations
````

4.- Once the migrations are assembled, we have to transfer them to our development environment.

````python
python3 manage.py migrate
````

5.- Once the migrations are assembled, we have to transfer them to our development environment.

````python
python3 manage.py migrate
````

6.- Although it is not mandatory, it is always good to create a super user for project administration.

````python
python3 manage.py createsuperuser
````

7.- After answering the questions for the superuser, we are ready for the project to run in all its dimensions.

````python
python3 manage.py runserver
````

Our project is running without problem, we can see it at http://127.0.0.1:8000/ as home page (page that we can later modify depending on the project)

Congratulations! You have a finctional Django project running right now!

The next step is to personalize this project in your own way, but now is time for you to work hard!