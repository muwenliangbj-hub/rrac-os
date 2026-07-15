import os
import importlib

class ModuleManager:
    def __init__(self, modules_dir='modules'):
        self.modules_dir = modules_dir
        self.loaded_modules = {}

    def scan_modules(self):
        """扫描并加载 modules 目录下的所有子模块"""
        if not os.path.exists(self.modules_dir):
            os.makedirs(self.modules_dir)
            return
        
        for module_name in os.listdir(self.modules_dir):
            if os.path.isdir(os.path.join(self.modules_dir, module_name)):
                self.load_module(module_name)

    def load_module(self, module_name):
        """动态导入模块"""
        try:
            module = importlib.import_module(f"{self.modules_dir}.{module_name}")
            self.loaded_modules[module_name] = module
            print(f"Module {module_name} loaded successfully.")
        except Exception as e:
            print(f"Failed to load module {module_name}: {e}")

    def get_module(self, module_name):
        return self.loaded_modules.get(module_name)

# 实例化并扫描
manager = ModuleManager()
manager.scan_modules()
