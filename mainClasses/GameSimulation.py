import pygame
from abc import ABC, abstractmethod

class GameWindow:
    def __init__(self, width, height, game_name):
        pygame.display.set_caption(game_name)

    def is_running(self):
        pass

    def clear(self):
        pass

    def refresh(self):
        pass


class GameSimulation(ABC):
    def __init__(self, width, height, title):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.running = True
        self.scenes = {}
        self.active_scene = None

    @abstractmethod
    def load_content(self):
        pass

    @abstractmethod
    def update(self, dt):
        pass

    @abstractmethod
    def draw(self):
        pass

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if self.active_scene:
                self.active_scene.handle_events(event)

    def switch_scene(self, scene_name):
        if scene_name in self.scenes:
            self.active_scene = self.scenes[scene_name]

    def add_scene(self, name, scene):
        self.scenes[name] = scene

    def run(self):
        self.load_content()
        while self.running:
            dt = self.clock.tick(60) / 1000
            self.handle_events()
            self.update(dt)
            if self.active_scene:
                self.active_scene.update(dt)
                self.active_scene.draw(self.screen)
            pygame.display.flip()
        pygame.quit()


class GameClock:
    def tick(self, param):
        pass