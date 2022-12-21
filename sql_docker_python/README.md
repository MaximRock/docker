#### Создание image:
$ sudo docker build -t pos_sql:v1 .

#### Запуска контейнера:
sudo docker run -p 5000:5000 --mount type=bind,source=/srv/app/conf/web.conf,destination=/srv/app/conf/web.conf --mount type=bind,source=/srv/app/web.py,destination=/srv/app/web.py cc01eca8c2f6
#### Screenshots
##### ubuntu
---

![12_1](https://user-images.githubusercontent.com/95434302/208957564-a8969f44-2a57-44a8-9ce4-56f81d4625fe.png)

---

![13_1](https://user-images.githubusercontent.com/95434302/208957596-a792484c-f36e-4907-884a-91c37d01048d.png)

---

##### windows

---

![11](https://user-images.githubusercontent.com/95434302/208958556-431f2c22-9ae8-4d59-a95d-d19579c4c8fd.png)

---

![12](https://user-images.githubusercontent.com/95434302/208958598-e7bf2871-6dbb-4ed8-90c2-976f08d341f3.png)

---
