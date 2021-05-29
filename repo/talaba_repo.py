from db import db
from model.talaba import Talaba
from repo.repo import Repo


class TalabaRepo(Repo):

    c = db.conn.cursor()

    def getAll(self):
        sql = "SELECT id, ism, familiya, sharif, tug_yil, guruh, yunalish FROM talaba_view;"
        self.c.execute(sql)
        tplist = self.c.fetchall()
        # print(tplist)
        return list(map(Talaba, tplist))

    def getById(self,id):
        super().getById(id)

    def add(self, data):
        sql = "INSERT INTO talaba (ism, familiya, sharif, tug_yil, guruh) VALUES (%s,%s,%s,%s,%s);"
        try:
            self.c.execute(sql, [data.ism, data.familiya, data.sharif, data.tug_yil, data.guruh])
            return True
        except:
            print("Talaba qo'shishda xatolik")
            return False

    def update(self, data):
        sql = "UPDATE public.talaba SET ism=%s, familiya = %s, sharif = %s, tug_yil = %s, guruh = %s WHERE id = %s;"
        self.c.execute(sql, [data.ism, data.familiya, data.sharif, data.tug_yil, data.guruh, data.id])
        return True



    def delete(self, data):

        return self.deleteById(data.id)



    def deleteById(self, id):
        sql = "DELETE FROM talaba WHERE id = %s"
        self.c.execute(sql, [id])
        return True