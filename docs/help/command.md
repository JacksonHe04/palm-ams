## 在端口启动，进行测试
``` bash
source ~/.bashrc
conda activate palm
cd /home/ubuntu/palm-ams/back-django
python manage.py runserver 0.0.0.0:8001
```
control + c 关闭

## 使用 uwsgi + nginx 启动部署
``` bash
source ~/.bashrc
conda activate palm
cd /home/ubuntu/palm-ams/back-django
/home/ubuntu/anaconda3/envs/palm/bin/uwsgi --ini /home/ubuntu/palm-ams/back-django/palm.ini
sudo nginx -s reload
```

## 关闭部署
``` bash
pkill -f uwsgi -9
```

## 检查 uwsgi 进程
``` bash
ps -ef | grep uwsgi
```

## 更换 nginx 配置文件
``` bash
sudo nano /etc/nginx/sites-available/palm
sudo rm /etc/nginx/sites-enabled/palm
sudo ln -s /etc/nginx/sites-available/palm /etc/nginx/sites-enabled/palm
sudo nginx -t
sudo nginx -s reload
```

## 测试 nginx
``` bash
sudo nginx -t
```

sudo systemctl reload nginx