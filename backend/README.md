
## lyadmin后端

注意：本后端python版本请选择3.9及以上

~~~bash
    
4. 安装依赖环境
	pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
5. 执行迁移命令：(使用sql脚本直接导入可忽略本步骤)
	python manage.py makemigrations
	python manage.py migrate
6. 初始化数据：(使用sql脚本直接导入可忽略本步骤)
	python manage.py init
7. 启动项目（初始账号：superadmin 密码：123456）
	python manage.py runserver 127.0.0.1:8000
    或使用 daphne (使用【终端服务】的需要使用此asgi方式部署来支持websocket):
    daphne -b 0.0.0.0 -p 8000 --proxy-headers application.asgi:application
    
    使用celery【计划任务】需要额外启动celery 和 beat（调度器）
    mac/linux:
    celery -A application worker -B -l info
    windows:(需要安装: pip install eventlet)
    celery -A application worker -P eventlet -l info
    celery -A application beat -l info

~~~

## 其他说明

[//]: # (1、使用本项目记得要更改application-->settings-->SECRET_KEY)

[//]: # (~~~bash)

[//]: # (可以运行python manage.py shell)

[//]: # (from django.core.management import utils)

[//]: # (utils.get_random_secret_key&#40;&#41;)

[//]: # (获取生成的新SECRET_KEY替换原来的老KEY)

[//]: # (~~~)
2、本项目可使用最新的python版本开发（python3.11.x已支持）、注意最新django版本安全问题，请及时更新安全稳定版本