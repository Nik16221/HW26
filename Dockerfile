FROM python:3.10

WORKDIR /flask_app_docker

COPY requirements.txt .
COPY app.py .

RUN python3.10 -m pip install --no-cache -r requirements.txt

COPY . .

CMD flask run -h 0.0.0.0 -p 80