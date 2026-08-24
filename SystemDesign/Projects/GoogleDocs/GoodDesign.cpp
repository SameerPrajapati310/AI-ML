#include<bits/stdc++.h>
using namespace std;

class Document{
    public:
       virtual string render()=0;
};

class TextDocument : public Document{
    private:
       string text;
    public:
        TextDocument(string text){
            this->text = text;
        }

        string render() override {
            return text;
        }
};

class ImageDocument : public Document{
    private:
       string imagePath;
    public:
       ImageDocument(string imagePath){
           this->imagePath = imagePath;
       }
       string render() override {
           return "Rendering Image Document: [" + imagePath + "]";
       }
};
class NewLineDocument : public Document{
    public:
       string render() override {
           return "\n";
       }
};
class NewSpaceDocument : public Document{
    public:
       string render() override {
           return "\t";
       }
};

class DocumentFactory{
    public:
         vector<Document*> documents; /// instead of keeping separate containers for each document type, you can put all kinds of documents into one vector:
    public:
        void addDocument(Document* element){
            documents.push_back(element);
        }
        string renderAllDocuments(){
            string result;
            for (auto it : documents){
                result += it->render(); /// C++ checks the actual object type behind each pointer and calls the correct function.
                // When you iterate, each element in the vector is a Document*. Because render() is virtual, 
                // C++ uses the object’s vtable (pointed by vptr) to decide which render() to call at runtime. 
                // That’s why the correct function for TextDocument, ImageDocument, etc., is automatically chosen.
            }
            return result;
        }


};

class Persistance{
    public:
         virtual void save(string data)=0;
};

class SaveToFile : public Persistance{
    public:
       void save(string data) override{
            ofstream file("document_GoodDesign.txt");
            if (file) {
                file << data;
                file.close();
                cout << "Document saved to document_GoodDesign.txt" << endl;
            }
            else{
                cout << "Error saving document to document.txt" << endl;
            }
       }
};

class DocumentEditor{
    public:
        DocumentFactory* document;
        Persistance* persistance;
        string renderedCache;
    public:
        DocumentEditor(DocumentFactory* document, Persistance* persistance) {
            this->document = document;
            this->persistance = persistance;
        }   
        void AddText(string text_add){
            document->addDocument(new TextDocument(text_add));
        }
        void AddImage(string path){
            document->addDocument(new ImageDocument(path));
        }
        void newline(){
            document->addDocument(new NewSpaceDocument());
        }
        void addNewLine(){
            document->addDocument(new NewLineDocument());
        }
        string renderDocument() {
            if(renderedCache.empty()) {
                renderedCache = document->renderAllDocuments();
            }
            return renderedCache;
}

};


int main(){

    DocumentFactory* factory = new DocumentFactory();
    Persistance* persistence = new SaveToFile();

    DocumentEditor* editor = new DocumentEditor(factory, persistence);
    editor->AddText("Hello, World! Welcome to my new Google Document.");
    editor->addNewLine();
    editor->newline();
    editor->AddImage("path/to/image.png");
    editor->addNewLine(); 
    editor->AddText("This is a new paragraph.");

    string rendered = editor->renderDocument();
    cout << rendered << endl;
    persistence->save(rendered);

    return 0;
}