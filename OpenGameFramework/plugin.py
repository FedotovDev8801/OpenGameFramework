import importlib
import os

class PluginManager:
    def __init__(self, plugins_folder="plugins"):
        # Initialize the plugins folder and dictionary of loaded plugins
        self.plugins_folder = plugins_folder
        self.plugins = {}

    def load_plugins(self):
        """
        Loads all Python plugins from the specified plugins folder.
        """
        if not os.path.exists(self.plugins_folder):
            os.makedirs(self.plugins_folder)

        for file in os.listdir(self.plugins_folder):
            if file.endswith(".py"):
                plugin_name = file[:-3]
                module = importlib.import_module(f"{self.plugins_folder}.{plugin_name}")
                self.plugins[plugin_name] = module

    def execute_plugin(self, plugin_name, *args, **kwargs):
        """
        Executes a plugin's main function.
        :param plugin_name: Name of the plugin to execute.
        """
        if plugin_name in self.plugins:
            plugin = self.plugins[plugin_name]
            if hasattr(plugin, "main"):
                plugin.main(*args, **kwargs)
            else:
                print(f"Plugin {plugin_name} does not have a 'main' function.")
        else:
            print(f"Plugin {plugin_name} is not loaded.")