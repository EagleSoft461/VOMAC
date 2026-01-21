import importlib
import os
from core.module_interface import ModuleInterface

class ModuleLoader:
    def __init__(self, modules_path="modules"):
        self.modules_path = modules_path
        self.loaded_modules = []

    def discover(self):
        modules = []

        if not os.path.exists(self.modules_path):
            return modules
        
        for folder in os.listdir(self.modules_path):
            path = os.path.join(self.modules_path, folder)
            if os.path.isdir(path):
                modules.append(folder)

        return modules
    
    def load(self, module_name):
        module_path = f"{self.modules_path}.{module_name}.module"
        module_module = importlib.import_module(module_path)

        if not hasattr(module_module, "Module"):
            raise Exception(f"Module {module_name} does not expose Module class")
        
        module_instance = module_module.Module()

        if not isinstance(module_instance, ModuleInterface):
            raise Exception(
                f"Module {module_name} does not implement ModuleInterface"
            )

        self.loaded_modules.append(module_instance)
        return module_instance
    
    def shutdown_modules(self):
        for module in self.loaded_modules:
            if hasattr(module, "shutdown"):
             module.shutdown()