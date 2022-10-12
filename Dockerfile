FROM python:3.10

ENV HOME / flask_app_docker
WORKDIR $HOME

COPY requirements.txt .
RUN python3.10 -m pip install --no-cache -r requirements.txt

COPY . .

ENTRYPOINT ["sh", "entrypoint.sh"]