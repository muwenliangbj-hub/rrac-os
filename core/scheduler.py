from typing import Any

class Scheduler:
    """
    任务调度器，负责接收任务、查找对应模块、调用并返回结果。
    """
    def __init__(self, modules: dict[str, Any]) -> None:
        """
        :param modules: 系统当前加载的所有模块字典
        """
        self.modules: dict[str, Any] = modules

    def dispatch(self, module_name: str, task: Any) -> Any:
        """
        调度任务到指定模块。
        
        :param module_name: 目标模块的名称
        :param task: 传递给模块的任务数据
        """
        target = module_name.lower()
        if target in self.modules:
            module = self.modules[target]
            # 第一版做简单调用，若模块有 execute 接口则执行，没有则直接返回默认声明
            if hasattr(module, "execute"):
                return module.execute(task)
            return f"{module_name.capitalize()} executed without custom logic."
        else:
            raise ValueError(f"Module '{module_name}' is not found.")
