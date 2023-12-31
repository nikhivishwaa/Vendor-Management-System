
## Project Requirements

`python 3.10 and above`<br>
`git bash CLI`<br>
`Visual Studio Code - Code Editor`<br>

## Project Setup : 

#### open git bash and run the following commands

###### Clone the project
```
git clone git@github.com:nikhivishwaa/Vendor-Management-System.git
```

###### Change Directory
```
cd Vendor-Management-System/
``` 

###### Prepare Python virtual environment
```
python -m venv env
```

###### Open vscode by this command
```
code .
```


#### Start new terminal in vscode and run following commands

###### activate venv if not acivated automatically
```
.\env\Scripts\activate
```

###### Download all Dependencies
```
pip install -r requirements.txt
```

###### Switch to the project
```
cd vemsys
```

##### Run commands for migrations
```
python manage.py makemigrations
```
```
python manage.py migrate
```


#### Run this commands to start Django server

```
python manage.py runserver
```

##### Admin Credentials to login in Django Admin Panel

username - `admin`<br><br>
password - `root@8000`<br><br>

###### Or create new admin by following command

```
python manage.py createsuperuser
```

