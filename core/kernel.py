from core.event_bus import EventBus
from core.module_loader import ModuleLoader
from core.scheduler import Scheduler
from typing import Dict, Any

class RRACKernel:
    """
    RRAC-OS 核心内核，负责系统生命周期管理与核心组件初始化。
    """
    def __init__(self) -> None:
        """初始化内核核心组件。"""
        self.event_bus: EventBus = EventBus()
        self.loader: ModuleLoader = ModuleLoader()
        self.scheduler: Scheduler | None = None
        self.modules: dict[str, Any] = {}

    def boot(self) -> None:
        """
        执行系统标准启动流程。
        """
        print("RRAC-OS Alpha v0.1")
        print("Booting Kernel...")
        
        # 1. 自动扫描并加载 modules/ 目录
        print("Scanning modules...")
        self.modules = self.loader.scan_and_load()
        
        # 2. 按照扫描到的模块输出加载状态
        for module_name in self.modules.keys():
            print(f"{module_name.capitalize()} Loaded")
            
        # 3. 初始化调度器
        self.scheduler = Scheduler(self.modules)
        
        print("Kernel Ready.")
        print("Scheduler Ready.")
        print("System Running...")

if __name__ == "__main__":
    kernel = RRACKernel()
    kernel.boot()
