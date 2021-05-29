from model.foydalanuvchi import Foydalanuvchi
from repo.repo import Repo
from db.db import conn


class ProfilRepo(Repo):
    cur = conn.cursor()

    def getAll(self):
        sql = "SELECT id, ism, familiya, login FROM public.foydalanuvchi";
        self.cur.execute(sql)
        tplist = self.cur.fetchall()

        return list(map(Foydalanuvchi, tplist))

    def getById(self, id):
        super().getById(id)

    def getByLoginAndPassword(self, login, password):
        sql = "SELECT id, ism, familiya, login FROM public.foydalanuvchi WHERE login ilike %s and parol like %s"
        self.cur.execute(sql, [login, password])
        a = self.cur.fetchall()
        if a:
            return Foydalanuvchi(a[0])
        else:
            return False


    def add(self, data):
        super().add(data)

    def update(self, data):
        super().update(data)

    def delete(self, data):
        super().delete(data)

    def deleteById(self, id):
        super().deleteById(id)