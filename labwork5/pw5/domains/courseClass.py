class course:
    def __init__(self, sID: str, sName: str, iCredit: int):
        self.id = sID
        self.name = sName
        self.credit = iCredit
            
    def __str__(self):
        return f"{self.id}"

    def getID(self):
        return self.id

    def getName(self):
        return self.name

    def getPoint(self):
        return self.credit
