from repo.yunalish_repo import YunalishRepo
from service.service import Service


class YunalishService(Service):
    yr = YunalishRepo()

    def getAll(self):
       return self.yr.getAll()

    def getById(self):
        super().getById()

    def add(self, data):
        return self.yr.add(data)

    def update(self, data):
        return self.yr.update(data)

    def delete(self, data):
        return self.yr.delete(data)

    def deleteById(self, id):
        return self.yr.deleteById(id)