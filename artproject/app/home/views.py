# coding:utf8
import tornado.web


class HomeHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db


class IndexHandler(HomeHandler):
    def get(self):
        url = self.request.path
        sql = "select id,name from tag"
        tags = self.db.execute(sql).fetchall()
        # 文章列表
        t = self.get_argument("t", 0)
        page = self.get_argument("page", 1)
        page = int(page)
        t = int(t)
        if t == 0:
            sql = "select count(*) from art"
        else:
            sql = "select count(*) from art where tag=%d" % t
        total = self.db.execute(sql).fetchone()[0]
        arr = dict(
            pagenum=0,
            total=0,
            prev=1,
            next=1,
            pagerange=range(1, 2),
            data=[],
            url=self.request.path,
            tags=tags,
            page=page,
            t=t
        )
        if total > 0:
            shownum = 20.0
            import math
            pagenum = int(math.ceil(total / shownum))
            if page < 1:
                self.redirect(self.request.path + "?page=%d&t=%d" % (1, t))
            if page > pagenum:
                self.redirect(self.request.path + "?page=%d&t=%d" % (pagenum, t))
            offset = (page - 1) * int(shownum)

            if t == 0:
                sql = "select id,title,info,img from art limit :offset,:limit"
                data = self.db.execute(sql, dict(offset=offset, limit=int(shownum))).fetchall()
            else:
                sql = "select id,title,info,img from art where tag=:tag limit :offset,:limit"
                data = self.db.execute(sql, dict(tag=t, offset=offset, limit=int(shownum))).fetchall()
            btnnum = 5
            if btnnum > pagenum:
                firstpage = 1
                lastpage = pagenum
            else:
                if page == 1:
                    firstpage = 1
                    lastpage = btnnum
                else:
                    firstpage = page - 2
                    lastpage = page + btnnum - 3
                    if firstpage < 1:
                        firstpage = 1
                    if lastpage > pagenum:
                        lastpage = pagenum
            prev = page - 1
            next = page + 1
            if prev < 1:
                prev = 1
            if next > pagenum:
                next = pagenum
            arr = dict(
                pagenum=pagenum,
                total=total,
                prev=prev,
                next=next,
                pagerange=range(firstpage, lastpage + 1),
                data=data,
                url=self.request.path,
                tags=tags,
                page=page,
                t=t
            )
        self.render("home/index.html", arr=arr)


class SearchHandler(HomeHandler):
    def get(self):
        key = self.get_argument("key", "")
        if key == "":
            self.redirect("/")
        else:
            page = self.get_argument("page", 1)
            page = int(page)
            sql = "select count(*) from art where title like :key or content like :key or info like :key"
            total = self.db.execute(sql, dict(key="%" + key + "%")).fetchone()[0]
            shownum = 10.0
            import math
            pagenum = int(math.ceil(total / shownum))
            if page < 1:
                self.redirect(self.request.path + "?page=%d&key=%s" % (1, key))
            if page > pagenum:
                self.redirect(self.request.path + "?page=%d&key=%s" % (pagenum, key))
            offset = (page - 1) * int(shownum)

            sql = "select a.id,a.title,a.img,a.info,t.name,a.addtime from art as a left join tag as t on a.tag = t.id where a.title like :key or a.content like :key or a.info like :key limit :offset,:limit"
            data = self.db.execute(sql, dict(key="%" + key + "%", offset=offset, limit=int(shownum))).fetchall()
            btnnum = 5
            if btnnum > pagenum:
                firstpage = 1
                lastpage = pagenum
            else:
                if page == 1:
                    firstpage = 1
                    lastpage = btnnum
                else:
                    firstpage = page - 2
                    lastpage = page + btnnum - 3
                    if firstpage < 1:
                        firstpage = 1
                    if lastpage > pagenum:
                        lastpage = pagenum
            prev = page - 1
            next = page + 1
            if prev < 1:
                prev = 1
            if next > pagenum:
                next = pagenum
            arr = dict(
                pagenum=pagenum,
                total=total,
                prev=prev,
                next=next,
                pagerange=range(firstpage, lastpage + 1),
                data=data,
                url=self.request.path,
                key=key,
                page=page
            )
            self.db.commit()
            self.db.close()
            self.render("home/search.html", arr=arr)


class DetailHandler(HomeHandler):
    def get(self):
        id = self.get_argument("id", None)
        if id == None:
            self.redirect("/")
        else:
            sql = "select id,title,content from art where id = %d" % int(id)
            art = self.db.execute(sql).fetchone()
            self.db.commit()
            self.db.close()
            self.render("home/detail.html", art=art)
