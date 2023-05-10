# Auto-capture

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
Go to client directory then
 
Register in server and get username and password, then when run application put username and password in it

### windows
Go to `client/bin/windows` and run main.exe file

### linux
Go to `client/bin/linux`
```
cd client/bin/linux
```
Run 
```
./main
```
may encounter the following problem when running on Linux.
```
OSError: X get_image failed: error 8 (73, 0, 1310)
```
For the solution, refer to the [link](https://stackoverflow.com/questions/75752576/pillow-imagegrab-grab-not-working-on-a-virtual-machine)


### Python script with
```
python main.py
```