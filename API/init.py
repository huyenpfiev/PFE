class Repository(object):
    def __init__(self, adapter=None):
        if not adapter:
            raise ValueError("Invalid repository implementation")
        self.client = adapter()

    def login(self, selector):
        return self.client.login(selector)
        
    def register(self,selector):
        return self.client.register(selector)
    def saveAcc(self,selector):
        return self.client.saveAcc(selector)

    def getPubs(self,selector):
        return self.client.getPubs(selector)