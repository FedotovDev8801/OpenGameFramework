from abc import abstractmethod, ABC


class Scene(ABC):
    def __init__(self):
        self.objects = []

    @abstractmethod
    def handle_events(self, event):
        pass

    @abstractmethod
    def update(self, dt):
        pass

    @abstractmethod
    def draw(self, screen):
        pass

    def add_object(self, obj):
        self.objects.append(obj)

    def remove_object(self, obj):
        self.objects.remove(obj)
