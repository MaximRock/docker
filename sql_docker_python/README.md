#### Создание image:
$ sudo docker build -t pos_sql:v1 .

#### Запуска контейнера:
sudo docker run -p 5000:5000 --mount type=bind,source=/srv/app/conf/web.conf,destination=/srv/app/conf/web.conf --mount type=bind,source=/srv/app/web.py,destination=/srv/app/web.py cc01eca8c2f6
#### Screenshots
---

![12_1](https://user-images.githubusercontent.com/95434302/208957564-a8969f44-2a57-44a8-9ce4-56f81d4625fe.png)

---

![13_1](https://user-images.githubusercontent.com/95434302/208957596-a792484c-f36e-4907-884a-91c37d01048d.png)
