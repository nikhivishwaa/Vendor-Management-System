
## Project Requirements

`python 3.10 and above`<br>
`git bash CLI`<br>
`Visual Studio Code - Code Editor`<br>

## Step 1 : Run the following commands to setup this project

#### open git bash and run the following commands

###### clone the project
```
git clone git@github.com:nikhivishwaa/Vendor-Management-System.git
```
###### Change Directory
```
cd Vendor-Management-System/
``` 
###### Prepare Python virtual environment
```
python -m venv env```
```
code .``` open vscode by this command<br><br>

#### Start new terminal in vscode and run following command
`.\env\Scripts\activate` - activate venv if not acivated automatically <br><br>
`pip install -r requirements.txt` - Download all Dependencies<br><br>
`cd vemsys` - Switch to the project<br><br>

##### Now run commands for migrations
```
python manage.py makemigrations
```
```
python manage.py migrate
```

##### Run following commands to start Django server

```
python manage.py runserver
```

##### Admin Credentials to login in Django Admin Panel

username - `admin`<br><br>
password - `root@8000`<br><br>

###### Or You can register yourself as Admin by following command

```
python manage.py createsuperuser
```

<p>now enter your credentials</p>