from abc import ABC,abstractmethod

class DocumentElement:
    @abstractmethod
    def render():
        pass

class AddText(DocumentElement):
    def __init__(self,text):
        self.text = text
    def render(self):
        return self.text

class AddImage(DocumentElement):
    def __init__ (self,image):
        self.image = image
    def render(self):
        ans = f"Image :{self.image}"
        return ans
class AddInline(DocumentElement):
    def __init__ (self):
        pass
    def render(self):
        return "\n"

class Document:
    def __init__ (self):
        self.document = []
    def add_element(self,dE):
        self.document.append(dE)
    def render(self):
        result = ""
        for doc in self.document:
            result += doc.render()
        return result

class Persistance(ABC):
    @abstractmethod
    def save():
        pass
class SQL(Persistance):
    def __init__ (self):
        pass
    def save(self):
        print("Saving to MySQL")

class DocumentEditor:
    def __init__ (self,document,storage):
        self.document = document
        self.storage = storage

    def add_text(self,text):
        self.document.add_element(AddText(text))
    def add_image(self,image):
        self.document.add_element(AddImage(image))
    def add_inline(self):
        self.document.add_element(AddInline())
    def render_document(self):
        ans = self.document.render()
        print(ans)
    def saveDoc(self):
        self.storage.save()


db = SQL()
doc = Document()

editor = DocumentEditor(doc,db)
editor.add_text("Hi my name is sameer")
editor.add_inline()
editor.add_image("xyz.jpg")

editor.render_document()

editor.saveDoc()


