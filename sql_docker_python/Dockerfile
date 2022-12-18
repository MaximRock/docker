FROM python:3.10-slim
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
CMD [ "python3", "/srv/app/web.py" ]

## первый этап
#FROM python:3.10 AS builder
#COPY requirements.txt .
## установка зависимостей в локальную директорию user (например, /root/.local)
#RUN pip install --user -r requirements.txt
## второй этап (без названия)
#FROM python:3.10-slim
#WORKDIR /srv
## копирование только установки зависимостей из образа первого этапа
#COPY --from=builder /root/.local/bin /root/.local
#COPY ./srv .
## обновление переменной среды PATH
#ENV PATH=/root/.local:$PATH
#CMD [ "python3", "/srv/app/web.py" ]


#FROM python:3.10-slim
#WORKDIR /srv
#COPY requirements.txt ./
#RUN pip install --no-cache-dir -r requirements.txt
#COPY . /srv
#CMD [ "python3", "/srv/app/web.py" ]
