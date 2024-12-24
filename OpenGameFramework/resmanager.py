import os
from pygame import image, mixer

class ResourceManager:
    def __init__(self, resource_folder="resources"):
        self.resource_folder = resource_folder
        self.images = {}
        self.sounds = {}

    def load_image(self, image_name):
        """
        Loads an image file from the resources folder.
        :param image_name: Name of the image file to load.
        :return: Pygame image object.
        """
        image_path = os.path.join(self.resource_folder, "images", image_name)
        if image_name not in self.images and os.path.exists(image_path):
            self.images[image_name] = image.load(image_path)
        return self.images.get(image_name, None)

    def load_sound(self, sound_name):
        """
        Loads a sound file from the resources folder.
        :param sound_name: Name of the sound file to load.
        :return: Pygame sound object.
        """
        sound_path = os.path.join(self.resource_folder, "sounds", sound_name)
        if sound_name not in self.sounds and os.path.exists(sound_path):
            self.sounds[sound_name] = mixer.Sound(sound_path)
        return self.sounds.get(sound_name, None)

# Example usage
if __name__ == "__main__":
    resource_manager = ResourceManager()
    player_image = resource_manager.load_image("player.png")
    player_sound = resource_manager.load_sound("jump.wav")

    if player_image:
        print("Player image loaded successfully.")
    else:
        print("Failed to load player image.")

    if player_sound:
        print("Player sound loaded successfully.")
    else:
        print("Failed to load player sound.")
