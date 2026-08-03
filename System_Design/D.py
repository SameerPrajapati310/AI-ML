from abc import ABC,abstractmethod

class Database(ABC):
    @abstractmethod
    def save(self):
        pass

class SQL(Database):
    def save(self,name):
        print(f"saving to SQL database {name}")

class Mongo(Database):
    def save(self,name):
        print(f"saving to Mongo database : {name}")

class UserInterface:
    def __init__ (self,db:Database):
        self.db = db
    def register(self,name):
        print("-------Registering-------")
        self.db.save(name)

sql = SQL()
ans = UserInterface(sql)
ans.register("sameer")

print("+++++++++++")

mongo = Mongo()
answer = UserInterface(mongo)
answer.register("xyz")

