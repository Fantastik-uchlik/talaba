from db import db
from model.yunalish import Yunalish
from repo.repo import Repo


class YunalishRepo(Repo):
    c = db.conn.cursor()

    def getAll(self):
        sql = "SELECT * FROM public.yunalish"
        self.c.execute(sql)
        tl = self.c.fetchall()
        return list(map(Yunalish,  tl))
    def getById(self, id):
        sql = "SELECT * FROM public.yunalish WHERE id = %s"
        self.c.execute(sql, [id])
        tl = self.c.fetch()
        return Yunalish(tl)
    def add(self, data):
        sql = "INSERT INTO yunalish (nom, kod) VALUES (%s, %s);"
        self.c.execute(sql, [data.nom, data.kod])

    def update(self, data):
        sql = "UPDATE public.yunalish SET nom=%s, kod = %s WHERE id = %s;"
        self.c.execute(sql, [data.nom, data.kod, data.id])
        return True

    def delete(self, data):
        # sql = "DELETE INTO public.yunalish(id) VALUES (%s);"
        # self.c.execute(sql,[data])
        # tl = self.c.fetchall()
        # return list(map(Yunalish, tl))
        sql = 'DELETE INTO public.talaba(id,nom,kod) VALUES (%s, %s, %s);'
        self.c.execute(sql, data)
        tplist = self.c.fetchall()
        return list(map(Yunalish, tplist))

    def deleteById(self, id):
        sql = "DELETE FROM yunalish WHERE id=%s"
        self.c.execute(sql,[id])

