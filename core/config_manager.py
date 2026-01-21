import yaml

class ConfigManager:
    def __init__(self, path="config.yaml"):
        with open(path, "r") as file:
            self.config = yaml.safe_load(file) or {}

    def get(self, key, deafult=None):
        return self.config.get(key, deafult)