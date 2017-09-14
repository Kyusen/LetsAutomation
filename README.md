# README

This README document the step to step for run the project


## Quick Start

### Basics

1. install dependencies
```sh
$ sudo apt-get install libffi-dev libssl-dev python3-dev
```

### Motivation of this system

* This system is a project of TCC that automate the home, and application the login security for access this system.

### Clone the project

```
$ git clone https://github.com/Kyusen/LetsAutomation.git
```

### Install the requirements

* In the root of project execute this command

* This project use the Python 3.5.2

```
$ pip install -r requirements.txt
```

### Run the Application

```
$ uwsgi config/lets_automation.ini
```

* or

```
$ python app.py
```

### Access this page

* Access this page and realize the login

[http://127.0.0.1:5000/auth/login](http://127.0.0.1:5000/auth/login)

* In the running the database is create with this user:

```
$ user: admin
$ password: admin
```

