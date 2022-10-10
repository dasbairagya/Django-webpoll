##How to Install Django on Windows: Step by Step Guide
 #Table of Contents
#Introduction
#Prerequisites

#Step 1 — Opening PowerShell
#Step 2 - Verifying Python Installation
```
> python -V
```
#Step 3 - Upgrading Pip

```
> python -m pip install --upgrade pip
```
#Step 4 - Creating a Project Directory
```
> mkdir django_project
> > cd django_project
```

#Step 5 - Creating the Virtual Environment
```
> python -m venv venv
```
#Step 6 - Activating the Virtual Environment
```
> venv\Scripts\activate
```
#Step 7 - Installing Django
```
(venv)> pip install django or (venv)> pip install django==3.1
 ```
#Step 8 - Creating the Django Project
```
(venv)> django-admin startproject test_project
```
Step 9 - Running the Development Server
```
cd test_project
(venv)> python manage.py runserve
```
