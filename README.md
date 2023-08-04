
# IELTS project 

Our project is about mock test for IELTS students. Project is devided in two parts.

- Frontend
- Backend

This project is created for Frontend

## Teachnologies

**Client:** HTML, JavaScript, Bootstrap, jQuery, Fontawsome etc.

**Server:** Django, SQLite3 


###  Student Features
- Student can Login, Register and View & Edit profile
- Writing test submit
- Listening test submit
- Reading test submit
- Speaking test submit
- Studnet can view thare score in sorting order

###  Teacher Features
- Teacher can Login, Register and View & Edit profile
- Teacher can post withing test questions
- Teacher can post lisning test questions
- Teacher can post reading test questions
- Teacher can post speaking test questions
- Teacher can view and give mark to student who submited test
- Teacher can view edit and delete the posted questions

## Minimum requirements
- ```Python 3.8```
- We highly recommend and only officially support the latest release of each series
## Installation

- We are runing backend server on port number 8000 so we can not run frontend server on same port. We have to use another port for run server. we are useing port 5000 for runing frontend.
- You can use another port
###
- First clone git repositry

```
    git clone https://github.com/Dhara-Ghediya/IELTS_eLearning_frontend.git
```
- Go to project 
```
    cd IELTS_eLearning_frontend
```
- Now, install all packages from requirement.txt
```
    pip install -r requirement.txt
```
- Now, run project on port 5000
```
    python manage.py runserver 5000
```
