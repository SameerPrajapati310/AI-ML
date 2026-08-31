from abc import ABC, abstractmethod

class FileSystem:
    @abstractmethod
    def ls(self):
        pass
    @abstractmethod
    def cd(self,name):
        pass
    @abstractmethod
    def open_all(self):
        pass

    @abstractmethod
    def isFolder(self):
        pass

class File(FileSystem):
    def __init__ (self,name):
        self.name =  name

    def ls(self,indent=0):
        print(self.name)

    def cd(self,name):
        return None

    def open_all(self,indent=0):
        print(" " * indent + self.name)

    def isFolder(self):
        return False

    def get_name(self):
        return self.name

class Folder(FileSystem):
    def __init__ (self,name):
        self.name = name
        self.childern = []

    def add(self,item):
        self.childern.append(item)

    def ls(self, indent=0):
        for item in self.childern:
            if item.isFolder():
                print(" " * indent + "+ " + item.get_name())
            else:
                print(" " * indent + item.get_name())

    def cd(self,target):
        for child in self.childern:
            if child.isFolder() and child.get_name() == target:
                return child

    def open_all(self,indent=0):
        print(" " * indent + "+ " + self.name)

        for child in self.childern:
                child.open_all(indent+4)

    def get_name(self):
        return self.name

    def isFolder(self):
        return True


if __name__ == "__main__":
    f1 = Folder("Practice")
    
    f1.add(File("SD.py"))

    f1.add(File("AI.py"))
    f1.add(Folder("Figma"))
    f1.add(Folder("Backend"))
    f2 = f1.cd("Backend")

    f2.add(File("img.jpg"))
    f2.add(File("img2.jpg"))

    f1.open_all()
    