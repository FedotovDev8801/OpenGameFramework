class EventSystem:
    def __init__(self):
        # Dictionary to hold event listeners
        self.listeners = {}

    def register_event(self, event_name, callback):
        """
        Registers a new event and its callback.
        :param event_name: Name of the event to register.
        :param callback: Function to call when the event is triggered.
        """
        if event_name not in self.listeners:
            self.listeners[event_name] = []
        self.listeners[event_name].append(callback)

    def emit_event(self, event_name, *args, **kwargs):
        """
        Triggers an event and calls all associated callbacks.
        :param event_name: Name of the event to emit.
        """
        if event_name in self.listeners:
            for callback in self.listeners[event_name]:
                callback(*args, **kwargs)


class Scene:
    def __init__(self, name):
        # Initialize a scene with its name and a list of entities
        self.name = name
        self.entities = []

    def add_entity(self, entity):
        """
        Adds an entity to the scene.
        :param entity: Entity object to add.
        """
        self.entities.append(entity)

    def update(self):
        """
        Updates all entities within the scene.
        """
        print(f"Updating scene: {self.name}")
        for entity in self.entities:
            entity.update()


class Entity:
    def __init__(self, name):
        # Initialize an entity with a name
        self.name = name

    def update(self):
        """
        Updates the entity.
        """
        print(f"Updating entity: {self.name}")


# Example usage
if __name__ == "__main__":
    # Initialize the event system
    event_system = EventSystem()
    
    # Register an event
    event_system.register_event("game_start", lambda: print("Game Started!"))
    event_system.emit_event("game_start")

    # Create and update a scene
    main_scene = Scene("Main Scene")
    player = Entity("Player")
    enemy = Entity("Enemy")

    main_scene.add_entity(player)
    main_scene.add_entity(enemy)
    main_scene.update()