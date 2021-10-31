# BrencoQuiz-khiati

![Project Image](https://i.ibb.co/WVzM688/brenco-logo-1.png)

> A simple quiz application.

---

### Table of Contents
A simple Django quiz application with built-in features from the framework.

- [Description](#description)
- [Technologies](#technologies)
- [How To Use](#how-to-use)
- [Demo](#demo)
- [License](#license)
- [Author Info](#author-info)

---

## Description
#### Authentication

  -  Basic authentication (default)
  -  Token authentication (django-rest)	
##### PS: 
In order to use the token authentication, access the following paths:

/api/auth/register/

/api/auth/login/

---
#### Admin

  -  Sign in
  -  Participate in Quiz and see his own Result
  -  View, create, update, delete Questions
  -  View, create, update, delete Categories
  - Filter questions by categories
  -  View, delete Results of users 

---
#### User

   - Sign up, Sign in
   - Filter questions by categories
   - Participate in Quiz and see his own Result
   
[Back To The Top](#BrencoQuiz-khiati)

---

## Technologies

- Django framework
- PostgreSQL (Local)
- Docker (Local)

### Django features used

- Django rest framework
- Django-forms
- Django-auth
- Django-filter
- Knox
- Jinja2
- WhiteNoise
- Gunicorn

[Back To The Top](#BrencoQuiz-khiati)

---

## How To Use

#### Installation
```html
$ pip install -r requirements.txt
```

#### Package model changes
```html
$ python manage.py makemigrations
```

#### Execute the changes into the database
```html
$ python manage.py migrate
```

#### Run the server
```html
$ python manage.py runserver
```
[Back To The Top](#BrencoQuiz-khiati)

---

## Demo
```html
https://brencoquiz-khiati.herokuapp.com
```
#### Super-user login

- username: rairon
- password: 111

[Back To The Top](#BrencoQuiz-khiati)

---

## License

MIT License

Copyright (c) [2021] [Khiati Walid]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.


[Back To The Top](#BrencoQuiz-khiati)

---
## Author Info

- LinkedIn - [@KhiatiWalid](https://www.linkedin.com/in/khiati-walid/)

