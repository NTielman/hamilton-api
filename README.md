# HAMILTON API
---


## Description
A REST API containing information on the cast, musical tracks, and roles found in the Hamilton musical.

## Languages, Libraries & Frameworks
* Python
* FastAPI
* Peewee
* SQLite
* Uvicorn


## Setup
1. Clone the repository and with Python3 create a virtual environment in the directory. `python3 -m venv <your_env_name>`
2. Activate the environment `source <your_env_name>/bin/activate`
3. Install the necessary dependencies `pip install -r requirements.txt`
4. Open up a Python interactive shell `python`
5. Import the create_db module from the directory "setup" within the shell `import setup.create_db`
6. Run `setup.create_db.add_db_data()` to create the database, followed by `exit()` to exit the interactive shell

You should now see a 'hamilton.db' database file appear in the "setup" directory.

7. Run `python api.py` to start up the API server
You can now query the API at http://127.0.0.1:8000
or read its documentation at http://127.0.0.1:8000/docs


## Video Demo
https://youtu.be/pqT8HnUO_Q8


#### Structure:
Hamilton-api/  
├── __init__.py  
├── .gitignore  
├── api.py  
├── README.MD  
├── requirements.txt  
├── setup/  
│   ├── __init__.py  
│   ├── create_db.py  
│   ├── models.py  
│   └── services.py  
└── data/  
    ├── __init__.py  
    ├── acts.py  
    ├── cast.py  
    ├── musical_info.py  
    ├── roles.py  
    └── songs.py  

#### __init__.py, setup/__init__.py, data/__init__.py:
this is a special file that tells the python interpreter to treat the directory it is in as a package. I mainly use it to be able to import modules and functions from files in different directories.

#### .gitignore:
this is another special file that tells git not to track any of the files/directories written inside of it

#### api.py:
contains the API endpoints, what optional queries are allowed, what information each path should return, and how to handle possible 404 exceptions. This is also the file from which the uvicorn server gets booted up.

#### requirements.txt:
contains all the versioned packages needed to run this  application

#### setup/create_db.py:
imports and combines all the data and helper functions from the different files in the data directory to create the database tables and populate them with the collected data

#### setup/models.py:
specifies the models and table schemes for all the tables that can be found in the database

#### setup/services.py:
using peewee ORM contains all the queries to insert and retrieve information from the database

#### data/acts.py:
hardcoded information on the acts of the Hamilton musical

#### data/cast.py:
hardcoded information on the cast of Hamilton musical

#### data/musical_info.py:
contains general information such as the release year, poster, and synopsis of the hamilton musical

#### data/roles.py:
contains data of all roles and characters that appear in the Hamilton musical

#### data/songs.py:
contains information on all the songs that appear in the hamilton musical