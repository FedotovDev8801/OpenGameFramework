from gameBase.gameScene import GameScene
from gameBase.objects import GameObject
from mainClasses.GameSimulation import GameSimulation


class MyGame(GameSimulation):
    def load_content(self):
        game_scene = GameScene()
        player = GameObject(100, 100, 50, 50, (255, 0, 0))
        game_scene.add_object(player)
        self.add_scene("main", game_scene)
        self.switch_scene("main")

    def update(self, dt):
        pass

    def draw(self):
        pass

if __name__ == "__main__":
    game = MyGame(800, 600, "My Game Engine")
    game.run()
