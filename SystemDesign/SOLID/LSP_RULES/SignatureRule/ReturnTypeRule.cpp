#include<bits/stdc++.h>
using namespace std;

class Animale{

};

class Dog : public Animale{

};

class Parent{
    public:
        virtual Animale* get_animal(){
           cout << "Getting animal of type DOG from Parent" << endl;
           return new Dog();
       }
};

class Child : public Parent{
    public:
        virtual Animale* get_animal() override {
            cout << "Getting animal of type Dog from Child" << endl;
            return new Dog();
        }
};

class Client{
    private:
       Parent* p;
    public:
       Client ( Parent* p){
        this->p = p;
       }
       void take_animal(){
           p->get_animal();
       }
};

int main(){
    Parent* p = new Parent();
    Child* c = new Child();
    Client* client_child= new Client(c);
    Client* client_parent = new Client(p);
    client_child->take_animal();
    client_parent->take_animal();

    delete client_child;
    delete client_parent;
    delete c;
    delete p;
    return 0;

}