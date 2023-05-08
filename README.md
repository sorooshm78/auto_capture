# Auto-capture

![index](https://drive.google.com/uc?export=view&id=1r3pdFqTDNMOXAi1Lzrv7nu6ixjxVGcih)

## Compatibility
* Python >= 3.10.6
## Installation

Clone the project
```
git clone https://github.com/sorooshm78/auto_capture
```

Install requirements
```
pip install -r requirements.txt
```
## Run server

Go to server directory then

Create all the migrations files (database migrations) required to run this App.
```
python manage.py makemigrations
```

Apply migrations
```
python manage.py migrate
```
Run server
```
python manage.py runserver
```
"auto_capture" app will start on 127.0.0.1:8000 (localhost).
 
## Run client 
Go to server directory then
 
Register in server and get username and password, then change config file in config.py and put username and password in it
```
USERNAME = "username"
PASSWORD = "password"

SHOT_TIME = 20  # second
```

Run with
```
python main_socket.py
```