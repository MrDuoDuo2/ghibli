# ghibli

为熟悉前后端分离开发方式，模仿 [How to Connect to an API with JavaScript](https://www.taniarascia.com/how-to-connect-to-an-api-with-javascript/) 编写一个DEMO。

## 环境依赖

* MySQL8.0+
* Python 3.7+

## 使用说明

### 安装项目依赖包

在 `cmd` 中进入本项目目录，执行 `pip install -r requirements.txt`

### 初始化配置文件

* 进入目录 `configs`，复制文件 `common-sample.ini`，新文件名称为：`common.ini`
* 进入目录 `configs`，复制文件 `log-sample.ini`，新文件名称为：`log.ini`

### 编辑配置文件

打开目录 `configs` 下的 `common.ini`，编辑其中关于数据库的配置参数。

### 配置数据库

使用 MySQL 管理工具新建数据库 `ghibli`，并指定字符集为 `utf8mb4` 。SQL命令为：

`CREATE DATABASE ghibli DEFAULT CHARACTER SET utf8mb4 DEFAULT COLLATE utf8mb4_unicode_ci;`

### 初始化数据库

使用 `PyCharm` 运行目录 `scripts` 下的 `init_db_tables.py`

### 运行

使用 `PyCharm` 运行 `app.py`，然后访问 http://127.0.0.1:8080/ 即可。
