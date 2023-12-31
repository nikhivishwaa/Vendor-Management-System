
## Project Requirements

```
Python 3.10 or above
git bash CLI
Visual Studio Code - Code Editor
Postman software (optional)
```


## Project Setup : 

#### Open git bash and run the following commands

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

###### Activate venv if not acivated automatically
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

#### Admin Credentials to login in Django Admin Panel

username - `   admin       `<br>
password - `   root@8000   `<br>

###### Create new admin by following command

```
python manage.py createsuperuser
```



## Make request from JS on API endpoints with authtoken

###### Get list of Vendors

```
const apiUrl = 'http://127.0.0.1:8000/api/vendors/';

// Replace 'YOUR_TOKEN_HERE' with the actual token
const token = 'YOUR_TOKEN_HERE';

// Make the API request
fetch(apiUrl, {
  method: 'GET',
  headers: {
    'Authorization': `Token ${token}`,
    'Content-Type': 'application/json',
    // Add other headers if needed
  },
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
```

###### Retrieve vendor data

```
const apiUrl = 'http://127.0.0.1:8000/api/vendors/{vendor_code}/';

// Replace 'YOUR_TOKEN_HERE' with the actual token
const token = 'YOUR_TOKEN_HERE';

// Make the API request
fetch(apiUrl, {
  method: 'GET',
  headers: {
    'Authorization': `Token ${token}`,
    'Content-Type': 'application/json',
    // Add other headers if needed
  },
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
```


###### Retrieve vendor performance metrics data
```
const apiUrl = 'http://127.0.0.1:8000/api/vendors/{vendor_code}/performance/';

// Replace 'YOUR_TOKEN_HERE' with the actual token
const token = 'YOUR_TOKEN_HERE';

// Make the API request
fetch(apiUrl, {
  method: 'GET',
  headers: {
    'Authorization': `Token ${token}`,
    'Content-Type': 'application/json',
    // Add other headers if needed
  },
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
```