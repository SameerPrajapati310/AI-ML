#include<bits/stdc++.h>
using namespace std;

class car{
    public:
       virtual void startengine() = 0;
       virtual void shiftgear(int val) = 0;
       virtual void accelerate() = 0;
       virtual void breakapplied() = 0;
       virtual void stopengine() = 0;
       virtual ~car(){};
};

class sportscar : public car {
    public:
       string brand;
       string model;
       bool engineOn;
       int gear;
       int speed;
    sportscar(string a, string b){
        this->brand = a;
        this->model = b;
        engineOn = false;
        gear = 0;
        speed = 0;
    }
    void startengine(){
        engineOn = true;
        cout<<brand<<" "<<model<<":  Engine started"<<endl;
    }
    void shiftgear(int val){
        if ( !engineOn ){
            cout<<"Cannot shift the gear car engine is turned off"<<endl;
        }
        gear = val;
        cout<<brand<<" "<<model<<": Gear changed to "<<val<<endl;
    }
    void accelerate(){
        if ( !engineOn ){
            cout<<"Cannot accelerate the car engine is turned off "<<endl;
        }
        speed += 20;
        cout<<brand<<" "<<model<<": Car accelerated to "<<speed<<endl;

    }
    void breakapplied(){
        if ( !engineOn ){
            cout<<"Cannot apply brake car engine is turned off"<<endl;
        }
        speed -= 20;
        cout<<brand<<" "<<model<<": Car deaccelerated to spped"<<speed<<endl;
    }
    void stopengine(){
        if ( !engineOn ){
            cout<<"Cannot stop the engine as engine is turned off"<<endl;
        }
        engineOn = false;
        cout<<brand<<" "<<model<<": Engine stopped"<<endl;
    }
};
int main() {
    car* car_one = new sportscar("tesla", "models");  

    car_one->startengine();     
    car_one->shiftgear(1);      
    car_one->accelerate();     
    car_one->breakapplied();    
    car_one->stopengine();      

    delete car_one; 
}
