# coding:utf8
from home.views import IndexHandler as home_index
from home.views import SearchHandler as home_search
from home.views import DetailHandler as home_detail

from admin.views import RegisterHandler as admin_register
from admin.views import LoginHandler as admin_login
from admin.views import TaglistHandler as admin_taglist
from admin.views import TageditHandler as admin_tagedit
from admin.views import TagdelHandler as admin_tagdel
from admin.views import ArtlistHandler as admin_artlist
from admin.views import ArteditHandler as admin_artedit
from admin.views import ArtdelHandler as admin_artdel
from admin.views import LogoutHandler as admin_logout
from admin.views import UploadHandler as admin_upload

home_urls = [
    (r"/", home_index),
    (r"/index.html", home_index),
    (r"/search.html", home_search),
    (r"/detail.html", home_detail),
]

admin_urls = [
    (r"/register\.html", admin_register),
    (r"/login\.html", admin_login),
    (r"/tag_list\.html", admin_taglist),
    (r"/tag_edit\.html", admin_tagedit),
    (r"/tag_del\.html", admin_tagdel),
    (r"/art_list\.html", admin_artlist),
    (r"/art_edit\.html", admin_artedit),
    (r"/art_del\.html", admin_artdel),
    (r"/logout.html", admin_logout),
    (r"/upload", admin_upload),
]

urls = home_urls + admin_urls
