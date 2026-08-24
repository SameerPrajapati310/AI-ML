from abc import ABC, abstractmethod

# ==================================================
# Decorator Pattern
# ==================================================

class INotification(ABC):
    @abstractmethod
    def notify(self):
        pass


class SimpleNotification(INotification):
    def __init__(self, text):
        self.text = text

    def notify(self):
        return self.text


class NotificationDecorator(INotification):
    def __init__(self, notification):
        self.notification = notification


class TimeStamp(NotificationDecorator):
    def notify(self):
        return "[2025-10-02 GMT] " + self.notification.notify()


class Signature(NotificationDecorator):
    def notify(self):
        return self.notification.notify() + " | youtube.com"


# ==================================================
# Observer Pattern
# ==================================================

class IObserver(ABC):
    @abstractmethod
    def update(self, channel_name, video):
        pass


class IChannel(ABC):

    @abstractmethod
    def add_observer(self, observer):
        pass

    @abstractmethod
    def remove_observer(self, observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass


class Channel(IChannel):

    def __init__(self):
        self.name = ""
        self.video = ""
        self.subscribers = []
        self.observers = []

    def set_name(self, name):
        self.name = name

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        if subscriber in self.subscribers:
            self.subscribers.remove(subscriber)

    def get_subscribers(self):
        return self.subscribers

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.name, self.video)

    def upload_video(self, notification):

        self.video = notification.notify()

        print("\n🎥 New Video Uploaded!\n")

        self.notify_observers()


# ==================================================
# Subscriber
# ==================================================

class Subscriber:

    def __init__(self, name):
        self.name = name
        self.strategies = []

    def add_strategy(self, strategy):
        self.strategies.append(strategy)


# ==================================================
# Singleton
# ==================================================

class YouTubeService:

    _instance = None

    def __init__(self):
        self.channel = Channel()

    @classmethod
    def get_instance(cls):

        if cls._instance is None:
            cls._instance = cls()

        return cls._instance

    def register_channel(self, name):
        self.channel.set_name(name)
        return self.channel

    def get_channel(self):
        return self.channel


# ==================================================
# Strategy Pattern
# ==================================================

class NotificationStrategy(ABC):

    @abstractmethod
    def send_notification(self, content):
        pass


class EmailStrategy(NotificationStrategy):

    def __init__(self, email):
        self.email = email

    def send_notification(self, content):
        print(f"📧 Email sent to {self.email}")
        print(content)


class SmsStrategy(NotificationStrategy):

    def __init__(self, number):
        self.number = number

    def send_notification(self, content):
        print(f"📱 SMS sent to {self.number}")
        print(content)


class PushStrategy(NotificationStrategy):

    def send_notification(self, content):
        print("🔔 Push Notification")
        print(content)


# ==================================================
# Observer Implementation
# ==================================================

class NotifyEngine(IObserver):

    def __init__(self, observable=None):

        if observable is None:
            observable = YouTubeService.get_instance().get_channel()

        self.observable = observable

        # Register itself as observer
        self.observable.add_observer(self)

    def update(self, channel_name, video):

        for subscriber in self.observable.get_subscribers():

            print("===================================")
            print(f"Hi      : {subscriber.name}")
            print(f"Channel : {channel_name}")
            print(f"Video   : {video}")

            for strategy in subscriber.strategies:
                strategy.send_notification(video)

            print("===================================\n")


# ==================================================
# Client Code
# ==================================================

youtube = YouTubeService.get_instance()

tech = youtube.register_channel("Tech With Codex")

# Register Observer
engine = NotifyEngine()

# Subscribers
sameer = Subscriber("Sameer")
sameer.add_strategy(EmailStrategy("sameer@gmail.com"))
sameer.add_strategy(SmsStrategy("+91-9999999999"))

rahul = Subscriber("Rahul")
rahul.add_strategy(EmailStrategy("rahul@gmail.com"))

amit = Subscriber("Amit")
amit.add_strategy(PushStrategy())

# Subscribe users
tech.subscribe(sameer)
tech.subscribe(rahul)
tech.subscribe(amit)

# Decorate notification
video = SimpleNotification("Python Observer Pattern Explained")
video = TimeStamp(video)
video = Signature(video)

print("Final Notification Content:")
print(video.notify())

# Upload video
tech.upload_video(video)