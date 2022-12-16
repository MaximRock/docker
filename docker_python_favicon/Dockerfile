FROM ubuntu:20.04
RUN apt-get update \
    && apt-get install -qy python3.10 python3-pip python3.8-dev \
    && rm -rf /var/lib/apt/lists/*
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD [ "python3", "app.py" ]
