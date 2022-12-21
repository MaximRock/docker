#### Создание image:
$ sudo docker build -t pos_sql:v1 .

#### Запуска контейнера:
sudo docker run -p 5000:5000 --mount type=bind,source=/srv/app/conf/web.conf,destination=/srv/app/conf/web.conf --mount type=bind,source=/srv/app/web.py,destination=/srv/app/web.py cc01eca8c2f6
##### Screenshots


![12_1](https://user-images.githubusercontent.com/95434302/208955364-2a9ee20c-7229-4bb5-8f4f-f49638cec719.png)

![13_1](https://user-images.githubusercontent.com/95434302/208955414-165535fb-b72c-4d04-b2a1-b07ad97cbae5.png)
