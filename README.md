# Auto-capture

Auto-capture gets screeshots from client periodically and shows it in server. It can also run commands in client and show the output in server.

These are some images of server:

![login](https://drive.google.com/uc?export=view&id=1DkgLjuJEfXAFmZqqwauLj0iDNnFzJ9k0)
![home](https://drive.google.com/uc?export=view&id=1gQLBvPpOEE8Dxi801W6c0skeBEGqmvYu)
![command](https://drive.google.com/uc?export=view&id=1moI93fX4-QmwEcWJj2d55btbVGtaRIh7)

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

Go to server directory and create all the migrations files (database migrations) required to run this App.
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
Get username and password by registering in server. Then go to client directory, run it, input username, password and interval in seconds. 

### Run in Windows
Go to `client/bin/windows` and run main.exe file.

### Run in Linux
Go to `client/bin/linux` and run
```
cd client/bin/linux
./main
```
Following problem may be occur when running on Linux
```
OSError: X get_image failed: error 8 (73, 0, 1310)
```
To fix that refer to [this](https://stackoverflow.com/questions/75752576/pillow-imagegrab-grab-not-working-on-a-virtual-machine)


### Run manually
```
python main.py
```