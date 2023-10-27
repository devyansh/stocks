We are running 2 Docker container for backend in Flask and Celery worker.

Follow following steps to run the project:

Install Docker Desktop: https://docs.docker.com/desktop/
Install Windows Subsystem for Linux (WSL): In Powershell run these commands wsl --install then wsl --update
Install Celery python package: pip install celery
Install Redis: pip install -U "celery[redis]"
