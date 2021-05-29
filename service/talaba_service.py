from repo.talaba_repo import TalabaRepo
from service.service import Service


class TalabaService(Service):
    talabaRepo = TalabaRepo()

    def getAll(self):
        return self.talabaRepo.getAll()

    def getById(self):
        super().getById()

    def add(self, data):
        return self.talabaRepo.add(data)

    def update(self, data):
        return self.talabaRepo.update(data)

    def delete(self, data):
        return self.talabaRepo.delete(data)

    def deleteById(self, id):
        return self.talabaRepo.deleteById(id)