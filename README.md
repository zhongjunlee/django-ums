## 介绍
这是一个基于 Django + MySQL + Bootstrap 开发的用户管理系统, 帮助你快速上手Python Web应用开发。

## 功能模块

| 模块     | 进度 | 功能点                         |
| :------- | :--- | :----------------------------- |
| 部门管理 | 完成 | 增删改查，搜索，分页           |
| 用户管理 | 完成 | 增删改查，搜索，分页           |
| 认证     | 完成 | 登录/验证码/修改密码           |
| 数据统计 | 完成 | echarts折线图，柱状图，饼图    |
| 文件上传 | 完成 | 解析文件到db，form表单上传图片 |

## 软件架构

前端：Jquery、Bootstrap
后端：Python3.11、Django5.0
数据库：MySQL8.0+


## 项目文档
http://t.csdnimg.cn/xZsZo

## 使用说明

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


#### 


