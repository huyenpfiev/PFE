from init import Repository
from DB import MongoRepository
from schema import UserSchema,ArticleSchema,CoauthorSchema

class Service(object):
    def __init__(self,client=Repository(adapter=MongoRepository)):
        self.client = client
    
    def login(self, user):
        us = self.client.login(user)
        return [self.dump(u) for u in us]

    def register(self,user):
        return self.client.register(user)

    def saveAcc(self,user):
        return self.client.saveAcc(user)

    def getPubs(self,user):
        userArray= self.client.getPubs(user)
        return [self.dump(u) for u in userArray]
        
    def dump(self, data):
        return UserSchema().dump(data).data

