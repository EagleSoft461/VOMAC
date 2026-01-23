import importlib
import os
from core.module_interface import ModuleInterface

class ModuleLoader:
    def __init__(self):
        # Dosya sistemi yolu
        self.base_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "modules"
        )

        # Python import path
        self.import_base = "modules"

        self.loaded_modules = []

    def discover(self):
        modules = []
        
        if not os.path.exists(self.base_path):
            return modules

        for folder in os.listdir(self.base_path):
            path = os.path.join(self.base_path, folder)

            if os.path.isdir(path) and not folder.startswith("__"):
                modules.append(folder)

        print("MODULES PATH:", self.base_path)
        print("FOUND:", os.listdir(self.base_path))

        return modules

    def load(self, module_name):
        module_path = f"{self.import_base}.{module_name}.module"

        module_module = importlib.import_module(module_path)

        if not hasattr(module_module, "Module"):
            raise Exception(
                f"Module '{module_name}' does not expose Module class"
            )

        module_instance = module_module.Module()

        if not isinstance(module_instance, ModuleInterface):
            raise Exception(
                f"Module '{module_name}' does not implement ModuleInterface"
            )

        self.loaded_modules.append(module_instance)
        return module_instance

    def shutdown_modules(self):
        for module in self.loaded_modules:
            module.shutdown()