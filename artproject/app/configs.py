# coding:utf8
import os
from admin.views import PageUI

base_dir = os.path.dirname(__file__)

configs = dict(
    template_path=os.path.join(base_dir, "templates"),
    static_path=os.path.join(base_dir, "static"),
    debug=False,
    xsrf_cookies=True,
    cookie_secret='425d0f63c10e4673ae79431b8415a78e',
    login_url="/login.html",
    ui_modules=dict(
        page=PageUI
    )
)
