from repo.profil_repo import ProfilRepo


class ProfilService:
    pr = ProfilRepo()
    def getByLoginAndPassword(self, login, password):
        return self.pr.getByLoginAndPassword(login, password)