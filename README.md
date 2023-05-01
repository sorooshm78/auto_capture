# check_child

## Usage
I am using python "3.10.6" version 

first step clone project
```
git clone https://github.com/sorooshm78/check_child/
```

and then install requirements  
```
pip install -r requirements.txt
```
## Server
Go to server directory and then run following commands 

This will create all the migrations file (database migrations) required to run this App.
```
python manage.py makemigrations
```

Now, to apply this migrations run the following command
```
python manage.py migrate
```
Just go into the code directory and type 
```
python manage.py runserver
```
"check_child" app will start on 127.0.0.1:8000 (Local Host).
 
## Client 
Go to client directory and then run following commands
 
After register in site, change config file in config.py and put username and password
```
USERNAME = "username"
PASSWORD = "password"

SHOT_TIME = 20  # second
```
### Http
Send screenshot with POST method 
```
python main_http.py
```

### WebSocket
Send screenshot with socket and listen to server
```
python main_socket.py
```