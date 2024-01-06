# django-ums

#### 介绍
基于Django Python Web框架 + MySQL + Bootstrap 开发的用户管理系统, 目前包括：部门管理、用户管理、认证-注册登录、文件上传等功能。

#### 软件架构
前端：Jquery、Bootstrap
后端：Python3.11、Django5.0
数据库：MySQL8.0+


#### 安装教程
https://blog.csdn.net/lizhongjun1005/article/details/135376007?spm=1001.2014.3001.5501

#### 使用说明

1.  在settings.py更改为你的数据库连接信息
2.  初始化表结构

```python
$ python manage.py makemigrations

$ python manage.py migrate
```

 3.启动app

```python
python manage.py runserver
```



访问页面：localhost:8000/login

完成！


#### 功能介绍
部门管理---》已完成
用户管理---》已完成
认证（注册/登录）---》已完成
数据统计---》开发中
文件上传---》待开发

