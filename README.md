# cw_backend_test_2
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

## Running the server (manual)
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
    set FLASK_APP=app:client_app
    flask run --host 0.0.0.0 --port CLIENT_PORT &
    ```
  - open another terminal and enter
    ```cmd
    set FLASK_APP=app:admin_app
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

## Running the server (docker)
### build the images
  - Client API image
    ```bash
    sudo docker build -t client_api -f Dockerfile_client \
    --build-arg CLIENT_HOST=<desired_client_host> \
    --build-arg CLIENT_PORT=<desired_client_port> \
    --build-arg ADMIN_HOST=<desired_admin_host> \
    --build-arg ADMIN_PORT=<desired_admin_port> \
    --build-arg SECRET_KEY=<your_secret_key> .
    ```
  - Admin API image
    ```bash
    sudo docker build -t client_api -f Dockerfile_admin \
    --build-arg CLIENT_HOST=<desired_client_host> \
    --build-arg CLIENT_PORT=<desired_client_port> \
    --build-arg ADMIN_HOST=<desired_admin_host> \
    --build-arg ADMIN_PORT=<desired_admin_port> \
    --build-arg SECRET_KEY=<your_secret_key> .
    ```

### run images
  - Client 
    ```bash
    sudo docker run -p <desired_client_port>:3000 client_api:latest
    ```
  - Admin 
    ```bash
    sudo docker run -p <desired_admin_port>:3001 client_api:latest
    ```

## View the Swagger API docs
  Visit the `/ui` route on any of the running container's urls with `http://<host>:<port>/ui`
  
  Example: `http://0.0.0.0:1759/ui`
