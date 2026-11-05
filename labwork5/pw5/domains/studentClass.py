class student:
    def __init__(self, sID: str, sName: str, sBirth: str):
        self.id = sID
        self.name = sName
        self.birth = sBirth

    def __str__(self):
        return f"{self.id}"

    def getID(self):
        return self.id

    def getName(self):
        return self.name

    def getDoB(self):
        return self.birth
