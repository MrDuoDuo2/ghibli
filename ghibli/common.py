#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import PurePath

from flask import Flask
from flask_cors import CORS
from happy_python import HappyConfigParser
from happy_python import HappyLog
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import Config


CONFIG_DIR = PurePath(__file__).parent / 'configs'
CONFIG_FILENAME = str(CONFIG_DIR / 'common.ini')
LOG_CONFIG_FILENAME = str(CONFIG_DIR / 'log.ini')

config = Config()
HappyConfigParser.load(CONFIG_FILENAME, config)

app = Flask('ghibli')
# 支持 JSON 显示中文
app.config['JSON_AS_ASCII'] = False
# 前端跨域设置
CORS(app, resources=r'/*')

hlog = HappyLog.get_instance(LOG_CONFIG_FILENAME)


engine = create_engine(
    'mysql+mysqlconnector://%s:%s@%s:%s/%s'
    % (config.db_user,
       config.db_password,
       config.db_host,
       config.db_port,
       config.db_name))
DBSession = sessionmaker(bind=engine)
session = DBSession()
