### 更新公告
v3.3(4/2/2019)<br>
添加了定时任务(django_crontab), 用来持续对 herokuapp 请求, 防止应用休眠.

v3.2<br>
优化了文本加密功能(页面显示与后台逻辑优化).<br>

v3.1<br>
bootstrap CDN, 配合 cloudflare CDN 使页面访问速度大幅提升.<br>


v3.0 春节更新<br>
更新了主页随机歌曲与文本加密功能.


往期更新:<br>
略...<br>


### 使用

##### 为了更方便的查阅 Python教程 而做.


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



