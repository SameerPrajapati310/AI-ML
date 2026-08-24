#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

// Observer Interface
class ISubscriber {
public:
    virtual void update(const string& videoTitle,
                        const string& channelName) = 0;
    virtual ~ISubscriber() {}
};

// Subject Interface
class IChannel {
public:
    virtual void subscribe(ISubscriber* subscriber) = 0;
    virtual void unsubscribe(ISubscriber* subscriber) = 0;
    virtual void notifySubscribers() = 0;
    virtual ~IChannel() {}
};

// Concrete Subject
class Channel : public IChannel {
private:
    vector<ISubscriber*> subscribers;
    string name;
    string latestVideo;

public:
    Channel(const string& name) : name(name) {}

    void subscribe(ISubscriber* subscriber) override {
        if (find(subscribers.begin(), subscribers.end(), subscriber) == subscribers.end()) {
            subscribers.push_back(subscriber);
        }
    }

    void unsubscribe(ISubscriber* subscriber) override {
        auto it = find(subscribers.begin(), subscribers.end(), subscriber);
        if (it != subscribers.end()) {
            subscribers.erase(it);
        }
    }

    void notifySubscribers() override {
        for (auto subscriber : subscribers) {
            subscriber->update(latestVideo, name);
        }
    }

    void uploadVideo(const string& title) {
        latestVideo = title;

        cout << "\n====================================\n";
        cout << name << " uploaded: " << latestVideo << endl;
        cout << "====================================\n";

        notifySubscribers();
    }
};

// Concrete Observer
class Subscriber : public ISubscriber {
private:
    string name;

public:
    Subscriber(const string& name) : name(name) {}

    void update(const string& videoTitle,
                const string& channelName) override {
        cout << "Hey " << name
             << ", " << channelName
             << " uploaded a new video: "
             << videoTitle << endl;
    }
};

int main() {

    Channel coderArmy("CoderArmy");

    // No relationship with any channel yet
    Subscriber varun("Varun");
    Subscriber tarun("Tarun");

    // Relationship starts here
    coderArmy.subscribe(&varun);
    coderArmy.subscribe(&tarun);

    coderArmy.uploadVideo("Observer Pattern Tutorial");

    coderArmy.unsubscribe(&varun);

    coderArmy.uploadVideo("Decorator Pattern Tutorial");

    return 0;
}