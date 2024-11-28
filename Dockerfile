FROM python:3.9-slim

COPY . /project/app
WORKDIR /project/app/app

RUN pip install -U pip
RUN pip install -r requirements/requirements.txt

CMD ["flask", "run", "--host=0.0.0.0"]