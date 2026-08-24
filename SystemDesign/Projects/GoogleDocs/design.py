# Crud operation
# render document
# save

from abc import ABC, abstractmethod

#RENDER
class Document(ABC):
    def __init__ (self):
        @abstractmethod
        def render():
            pass

class AddText(Document):
    def __init__ (self,text):
        self.text = text
    def render(self):
        return self.text

class AddImage(Document):
    def __init__ (self,image):
        self.image = image
    def render(self):
        return "Image :" + self.image
    
class Newline(Document):
    def __init__ (self):
        pass
    def render(self):
        return "\n"

#CRUD
class DocumentElement:
    def __init__ (self):
        self.documents = []  # This will store list of Document
    def add_elements(self,element):
        self.documents.append(element)
    def get_elements(self):
        return self.documents
    def render(self):
        ans = ""
        for element in self.documents:
            ans += element.render()
        return ans

# STORAGE
class Persistance(ABC):
    @abstractmethod
    def save(self):
        pass

class SaveSQL(Persistance):
    def save(self):
        print("Saving to SQL")
        return 

class SaveToMyFile(Persistance):
    def save(self):
        print("Saving to MyFile")
        return

class DocumentEditor:
    def __init__ (self,doc,storage):
        self.documents = doc
        self.storage = storage
        self.answer = ""
    def addText(self,txt):
        self.documents.add_elements(AddText(txt))
    def addImage(self,image):
        self.documents.add_elements(AddImage(image))
    def newLine(self):
        self.documents.add_elements(Newline())

    def render(self):
        doc = self.documents.get_elements()
        for element in doc:
            self.answer += element.render()
        print(self.answer)



factory = DocumentElement()
store = SaveSQL()

editor = DocumentEditor(factory,store)

editor.addText("Hi my name is SAMeeR")
editor.newLine()
editor.addText("Hi i Am an AI")
editor.newLine()
editor.addImage("alienX.jpeg")
editor.newLine()

editor.render()

    
