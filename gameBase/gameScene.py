from mainClasses.sceneClass import Scene


class GameScene(Scene):
    def __init__(self):
        super().__init__()

    def handle_events(self, event):
        pass

    def update(self, dt):
        for obj in self.objects:
            obj.update(dt)

    def draw(self, screen):
        screen.fill((0, 0, 0))
        for obj in self.objects:
            obj.draw(screen)
