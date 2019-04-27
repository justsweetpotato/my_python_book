#### 为了更方便的查阅 Python 相关文档、教程而做.

 <i><b>警告: 不要直接 clone 这个项目, 静态资源异常的巨大...</b></i> 

### 使用

nginx 配置<br>
/etc/nginx/sites-available/default
```
server {
    charset utf-8;
    listen 80;
    server_name www.sweetpotato.xyz sweetpotato.xyz;
    
    location / {
        proxy_set_header Host $host;
        proxy_pass http://127.0.0.1:8000;
    }

    location /static {
        alias /root/my_python_book/static;
    }
}
```

注意给 root 文件夹加上可执行权限
```
chmod +x root
```
重启 Nginx
```
nginx -s reload
```

gunicorn 启动命令
```
nohup gunicorn django_book.wsgi:application -c gunicorn.conf.py &
```

定时任务
```
# 添加定时任务到系统中
python manage.py crontab add

# 显示已经激活的定时任务
python manage.py crontab show

# 移除定时任务
python manage.py crontab remove
```
