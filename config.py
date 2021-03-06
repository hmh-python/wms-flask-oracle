# -*- coding:utf-8 -*-

import os
import cx_Oracle


basedir = os.path.abspath(os.path.dirname(__file__))
conn = cx_Oracle.connect('xxxxuser/xxxxpassword@138.10.198.223:1521/orcl')


class Config(object):
    os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
    SQLALCHEMY_POOL_SIZE = 20
    SQLALCHEMY_POOL_TIMEOUT = 5 # 指定数据库连接池的超时时间。默认是10s。
    SQLALCHEMY_POOL_RECYCLE = 3000 # 配置连接池的 recyle 时间。默认是7200s。
    SECRET_KEY = 'hmh-crvanguard-1q@w#e$R'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    OUSI_POSTS_PER_PAGE = 20


    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                            'oracle+cx_oracle://xxxxuser:%s@138.10.198.223:1521/orcl' % 'xxxxpassword'


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
                            'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                            'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
