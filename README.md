
# IELTS project 

This project is about mock tests for IELTS students. project is divided into two parts.

- Frontend
- Backend

This project is created for Frontend

## Teachnology 

**Client:** HTML, javascript, bootstrap, jquery,  font awesome, etc.

**Server:** Django, sqlite3 



###  student Features
- Students can login,register and view profile
- writing test submit
- lisning test submit
- reading test submit
- speaking test submit
- students can view their scores in sorting order

###  Teacher Features
- the teacher can login, register and view profile
- the teacher can post writing test questions
- the teacher can post listening test questions
- a teacher can post reading test questions
- a teacher can post speaking test questions
- teacher can view and give marks to students who submit test
- a teacher can view edit and delete the posted questions

## minimum requrement
- ```Python 3.8```
- We highly recommend and only officially support the latest release of each series
## Installation

- we are running the backend server on port number 8000 so we can not run the frontend server on the same port. we have to use other ports to run the server. we are useing port 5000 for runing frontend 
- you can use other port
###
- First clone git repository

```
    git clone https://github.com/Dhara-Ghediya/IELTS_eLearning_frontend.git
```
- go to project 
```
    cd IELTS_eLearning_frontend
```
- now install all packages from requirement.txt
```
    pip install -r requirement.txt
```
- now run a project on port 5000
```
    python manage.py runserver 5000
```

## Note
if you are changing a backend server port or its address than in 

IELTS_eLearning_frontend


    └── IELTS_eLearning_frontend
        └── localsetting.py

- there we define variables for call backend APIs
  
- `url=` give your backend server URL
- `media_url=` give a backend server URL
