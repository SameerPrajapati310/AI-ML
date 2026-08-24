#include<bits/stdc++.h>
using namespace std;

class Talkable{
    public: 
        virtual void talk() = 0;
};
class NormalTalk : public Talkable{
public:
    void talk() override {
        cout << "Normal Talk" << endl;
    }
};
class NoTalk : public Talkable{
    public:
        void talk() override{
            cout << "No Talk" << endl;
        }
};

class Walkable{
    public:
        virtual void walk() = 0;
};
class NormalWalk : public Walkable{
    public:
        void walk() override{
            cout << "Normal Walk" << endl;
        }
};

class NoWalk : public Walkable{
    public:
        void walk() override{
            cout << "No Walk" << endl;
        }
};

class FlyAble{
    public:
        virtual void fly() = 0;
};
class NormalFly : public FlyAble{
    public:
        void fly() override{
            cout << "Normal Fly" << endl;
        }
};
class NoFly : public FlyAble{
    public: 
        void fly() override{
            cout << "No Fly" << endl;
        }
};

class Robot{
    public:
       Talkable* talkBehavior;
       Walkable* walkBehavior;
       FlyAble* flyBehavior;

       Robot(Talkable* tb, Walkable* wb, FlyAble* fb) {
           this->talkBehavior = tb;
           this->walkBehavior = wb;
           this->flyBehavior = fb;
       }

       void performTalk() {
           talkBehavior->talk();
       }

       void performWalk() {
           walkBehavior->walk();
       }

       void performFly() {
           flyBehavior->fly();
       }
};

class CompanionRobot : public Robot {
    public:
        CompanionRobot(Talkable* tb, Walkable* wb, FlyAble* fb) : Robot(tb, wb, fb) {}
};

int main(){
    CompanionRobot* robot = new CompanionRobot(new NormalTalk(), new NormalWalk(), new NormalFly());
    robot->performTalk();
    robot->performWalk();
    robot->performFly();
    delete robot;
    return 0;
}