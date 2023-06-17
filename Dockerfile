FROM python:3.10-alpine
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app
ENTRYPOINT [ "python" ]
CMD ["main.py" ]
