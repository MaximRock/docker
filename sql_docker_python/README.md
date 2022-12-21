#### Создание image:
$ sudo docker build -t pos_sql:v1 .

#### Запуска контейнера:
sudo docker run -p 5000:5000 --mount type=bind,source=/srv/app/conf/web.conf,destination=/srv/app/conf/web.conf --mount type=bind,source=/srv/app/web.py,destination=/srv/app/web.py cc01eca8c2f6
##### Screenshots

![img](https://drive.google.com/file/d/1olzpQxHU3E-BBJnbI9XtxzXioOG8_SHw/view?usp=share_link)

![](https://drive.google.com/file/d/1WXp5iSDf-r_6eHoF2U03-a9z_rHmVLwO/view?usp=share_link)