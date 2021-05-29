from repo.guruh_repo import GuruhRepo


class GuruhService:
    repo = GuruhRepo()

    def getAll(self):
        return self.repo.getAll()

    def getById(self, id):
        return self.repo.getById(id)

    def add(self, data):
        return self.repo.add(data)

    def update(self, data):
        return self.repo.update(data)
    def deleteById(self, data):
        return self.repo.deleteById(data)

    def getByYunalish(self, yunalish_id):
        return self.repo.getByYunalish(yunalish_id)
