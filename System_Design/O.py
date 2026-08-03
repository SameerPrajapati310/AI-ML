#Open close Principle

from abc import ABC,abstractmethod
class Database:
    @abstractmethod
    def save(self):
        pass


class SQLdatabase(Database):
    def save(self,name):
        print("saving to SQL")

class Mongodatabase(Database):
    def save(self,name):
        print("saving to MongoDB")


ans = SQLdatabase()
ans.save("Sameer")
answer = Mongodatabase()
answer.save("xyz")
    