# coding:utf8
import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options

from tornado.options import options, define
from configs import configs
from urls import urls

define("port", type=int, default=8002)
define("db_host", default="127.0.0.1", type=str)  # 指定数据库IP
define("db_user", default="root", type=str)  # 指定数据库用户名
define("db_pwd", default="root", type=str)  # 指定数据库密码
define("db_name", default="artdb", type=str)  # 指定数据库名称
define("db_port", default=3306, type=int)  # 指定数据库端口

from sqlalchemy import create_engine
import pymysql
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(
    'mysql+pymysql://%s:%s@%s:%d/%s' % (
        options.db_user,
        options.db_pwd,
        options.db_host,
        options.db_port,
        options.db_name
    ),
    encoding='utf-8',
    echo=False,
    pool_size=100,
    pool_recycle=7200,
    connect_args={'charset': 'utf8'}
)


class CustomApplication(tornado.web.Application):
    def __init__(self, configs, urls):
        settings = configs
        handlers = urls
        super(CustomApplication, self).__init__(handlers=handlers, **settings)
        self.db = scoped_session(
            sessionmaker(
                bind=engine,
                autocommit=False,
                autoflush=True,
                expire_on_commit=False
            )
        )


def create_app():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(CustomApplication(configs, urls))
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


app = create_app
