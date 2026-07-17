import os
import importlib
from typing import Dict, Any

class ModuleLoader:
    """
    自动扫描 modules/ 目录并加载所有 RRAC 模块。
    """
    def __init__(self, target_dir: str = "modules") -> None:
        """
        :param target_dir: 扫描的目标目录，默认为 modules
        """
        self.target_dir: str = target_dir

    def scan_and_load(self) -> dict[str, Any]:
        """
        扫描包含 __init__.py 的目录并将其自动载入。
        
        :return: 已加载的模块字典 {模块名: 模块对象}
        """
        loaded_modules: dict[str, Any] = {}
        
        if not os.path.exists(self.target_dir):
            return loaded_modules

        for item in os.listdir(self.target_dir):
            item_path = os.path.join(self.target_dir, item)
            # 凡是包含 __init__.py 的目录，都自动识别为 RRAC 模块
            if os.path.isdir(item_path) and os.path.isfile(os.path.join(item_path, "__init__.py")):
                try:
                    module_path = f"{self.target_dir}.{item}"
                    # 动态导入模块
                    imported_module = importlib.import_module(module_path)
                    loaded_modules[item.lower()] = imported_module
                except Exception as e:
                    print(f"Error loading module {item}: {e}")
                    
        return loaded_modules
