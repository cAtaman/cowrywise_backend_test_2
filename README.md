# cowrywise_backend_test_2
API for The Software Engineer (Backend) role second assessment


## Setup Instructions

- Clone this repo
```bash
git clone https://github.com/cAtaman/cowrywise_backend_test_2.git
```

- Navigate to the project's root and start a virtual environment 
```bash
cd cowrywise_backend_test_2
```

- Create a virtual environment with python3
```bash
python3 -m virtualenv venv
```

- Activate the virtual environment with the following command:

  - Linux 
    ```bash
    source venv/bin/activate
    ```

  - Windows
    ```cmd
    venv/Scripts/activate
    ```


- Install all dependencies
```bash
pip install -r requirements.txt
```

- Run tests
```bash
pytest tests.py
```

## To run the server
###### Notes 
  - `CLIENT_PORT` is the port you want the client API to run at
  - `ADMIN_PORT` is the port you want the admin API to run at

  - Linux
```bash
chmod +x run.sh
./run.sh <CLIENT_PORT> <ADMIN_PORT>
```

- Windows
  - open a terminal and enter
    ```cmd
    set FLASK_APP=src.client.wsgi:app
    flask run --host 0.0.0.0 --port CLIENT_PORT &
    ```
  - open another terminal and enter
    ```cmd
    set FLASK_APP=src.admin.wsgi:app
    flask run --host 0.0.0.0 --port ADMIN_PORT &
    ```

The client API can be accessed at
```
http://localhost:CLIENT_PORT/
```

while the admin API is at 
```
http://localhost:ADMIN_PORT/
``` 

