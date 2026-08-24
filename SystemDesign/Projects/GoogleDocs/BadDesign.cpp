#include<bits/stdc++.h>
using namespace std;

class DocumentElement{
    private:
        vector<string> documents;
        string renderDocument;
    public:
        void addText(string text){
            documents.push_back(text);
        }
        void addImage(string imagePath){
            documents.push_back(imagePath);
        }
        string render(){
            if (renderDocument.empty()){
                string result;
                for ( auto doc : documents ){
                    if ( doc.substr(doc.size()-4) == ".jpg" || doc.substr(doc.size()-4) == ".png" ){
                        result += "[Image:"+doc+"]"+"\n";
                    } else {
                        result += doc+"\n";
                    }
                }
                renderDocument = result;
            }
            return renderDocument;
        }
        void SaveToFile(){
            ofstream file("document.txt");
            if (file.is_open()){
                file<<render();
                file.close();
                cout<<"Documment saved to document.txt";
            }
            else{
                cout<<"Not able to open file";
            }
        }
};


int main(){
    DocumentElement* doc = new DocumentElement;
    doc->addText("Hello World!! My first GoogleDocs with BadDesign!!!");
    doc->addImage("image.jpg");
    doc->SaveToFile();
    delete doc;
    return 0;
}