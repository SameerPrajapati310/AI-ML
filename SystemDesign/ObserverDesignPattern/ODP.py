from abc import ABC,abstractmethod

class Ichannel:
    @abstractmethod
    def subscribe(self):
        pass

    @abstractmethod
    def unsubscribe(self):
        pass

    @abstractmethod
    def notify(self):
        pass

class Isubscriber:
    @abstractmethod
    def update(self):
        pass

class Channel(Ichannel):
    def __init__ (self,name):
        self.name = name
        self.latest_video = None
        self.subscribers = {}
    def subscribe(self,user_name):
        if user_name not in self.subscribers:
            self.subscribers[user_name] = True

    def unsubscribe(self, user_name):
        if user_name in self.subscribers:
            del self.subscribers[user_name]

    def notify(self):
        for key,val in self.subscribers.items():
            key.update(self.latest_video,self.name)

    def upload_video(self,video_title):
        self.latest_video = video_title
        self.notify()


class Subscriber(Isubscriber):
    def __init__ (self,name):
        self.name = name


    def update(self,video_name,channel_name):
        print("Hi",self.name)
        print("From :",channel_name)
        print("New video Uploaded :", video_name)
        print("="*40)
        

channel = Channel("Marvel")

user1 = Subscriber("Sameer")
user2 = Subscriber("Rishu")

channel.subscribe(user1)
channel.subscribe(user2)

channel.upload_video("Spider Man : Brand New Day")

channel.unsubscribe(user2)
channel.upload_video("Avengers : DoomsDay")