from mainClasses import GameSimulation

class GameNCBuild:
    def __init__(self, game_name, width, height):
        self.game_name = game_name
        self.width = width
        self.height = height
        self.screen = GameSimulation.GameWindow(width, height, game_name)
        self.clock = GameSimulation.GameClock()
        self.scenes = {}
        self.current_scene = None

    def add_scene(self, scene_name, scene):
        self.scenes[scene_name] = scene

    def set_scene(self, scene_name):
        if scene_name in self.scenes:
            self.current_scene = self.scenes[scene_name]

    def run(self):
        while self.screen.is_running():
            self.clock.tick(60)
            self.screen.clear()
            if self.current_scene:
                self.current_scene.update(self.screen)
            self.screen.refresh()

class Scene:
    def __init__(self):
        self.objects = []

    def add_object(self, obj):
        self.objects.append(obj)

    def update(self, screen):
        for obj in self.objects:
            obj.update(screen)

class GameObject:
    def __init__(self, x, y, sprite):
        self.x = x
        self.y = y
        self.sprite = sprite

    def update(self, screen):
        screen.draw(self.sprite, self.x, self.y)

engine = GameNCBuild("My First Game", 800, 600)

main_scene = Scene()

player = GameObject(100, 150, "player_sprite.png")
main_scene.add_object(player)

engine.add_scene("MainScene", main_scene)

engine.set_scene("MainScene")
engine.run()