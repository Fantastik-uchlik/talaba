from db.db import conn
from model.guruh import Guruh


class GuruhRepo:
    cur = conn.cursor()

    def getAll(self):
        sql = "SELECT id, nom, yunalish, yil FROM guruh;"
        self.cur.execute(sql)
        tplist = self.cur.fetchall()

        return list(map(Guruh, tplist))

    def getById(self, id):
        sql = "SELECT id, nom, yunalish, yil FROM guruh WHERE id = %s;"
        self.cur.execute(sql, [id])
        return Guruh(self.cur.fetch())

    def getByYunalish(self, yunalish_id):
        sql = "SELECT id, nom, yunalish, yil FROM guruh WHERE yunalish = %s;"
        try:
            self.cur.execute(sql, [yunalish_id])
            tplist = self.cur.fetchall()

            return list(map(Guruh, tplist))
        except:
            return False


    def add(self, g):
        sql = "INSERT INTO guruh(nom, yunalish, yil) VALUES(%s, %s, %s)"
        self.cur.execute(sql, [g.nom, g.yunalish, g.yil])

    def update(self, g):
        sql = "UPDATE public.guruh SET nom = %s, yunalish = %s, yil = %s WHERE id = %s"
        self.cur.execute(sql, [g.nom, g.yunalish, g.yil, g.id])
        return True
    def deleteById(self, g):
        sql = "DELETE FROM guruh WHERE id = %s"
        self.cur.execute(sql, [g])