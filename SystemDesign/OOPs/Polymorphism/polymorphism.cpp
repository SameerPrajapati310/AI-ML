#include <bits/stdc++.h>
using namespace std;

class car {
protected:
    string brand;
    string model;
    bool engine;
    int speed;

public:
    car(string a, string b) {
        brand = a;
        model = b;
        engine = false;
        speed = 0;
    }
    void startengine() {
        engine = true;
        cout << brand << " " << model << ": Engine started" << endl;
    }
    void stopengine() {
        engine = false;
        cout << brand << " " << model << ": Engine stopped" << endl;
    }
    virtual void accelerate() = 0;
    virtual void brake() = 0;
    virtual void showSpeed() = 0;
    virtual ~car() {}
};

class manual : public car {
public:
    int gear;
    manual(string a, string b) : car(a, b) {
        gear = 0;
    }
    void changegear(int g) {
        gear = g;
        cout << brand << " " << model << ": Changed to gear " << gear << endl;
    }
    void accelerate() override {
        speed += 40;
        cout << brand << " " << model << ": Accelerating to " << speed << " km/h" << endl;
    }
    void brake() override {
        speed = max(0, speed - 20);
        cout << brand << " " << model << ": Slowing down to " << speed << " km/h" << endl;
    }
    void showSpeed() override {
        cout << brand << " " << model << ": Current speed is " << speed << " km/h" << endl;
    }
};

class electric : public car {
public:
    int battery_capacity;
    electric(string a, string b) : car(a, b) {
        battery_capacity = 100;
    }
    void accelerate() override {
        if (battery_capacity == 0) {
            cout << brand << " " << model << ": Battery is low, please charge the car" << endl;
        } else {
            speed += 30;
            battery_capacity -= 10;
            cout << brand << " " << model << ": Accelerating to " << speed << " km/h" << endl;
        }
    }
    void brake() override {
        speed = max(0, speed - 20);
        cout << brand << " " << model << ": Slowing down to " << speed << " km/h" << endl;
    }
    void showSpeed() override {
        cout << brand << " " << model << ": Current speed is " << speed << " km/h" << endl;
    }
};

int main() {
    car* car_one = new manual("Tata", "Nano");
    car* car_two = new electric("Tesla", "Model S");

    car_one->startengine();
    car_one->accelerate();
    car_one->brake();
    car_one->showSpeed();
    car_one->stopengine();

    cout << "-------------------------" << endl;

    car_two->startengine();
    car_two->accelerate();
    car_two->brake();
    car_two->showSpeed();
    car_two->stopengine();

    delete car_one;
    delete car_two;

    return 0;
}
