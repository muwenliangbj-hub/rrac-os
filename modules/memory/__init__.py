from modules.memory.memory_manager import MemoryManager
from typing import Dict, Any

# 实例化当前模块的管理中心
_manager = MemoryManager()

def execute(action_data: dict[str, Any]) -> dict[str, Any]:
    """
    供内核调度器（Scheduler）调用的统一执行接口。
    
    期望的 action_data 格式：
    {
        "action": "save" | "query" | "delete" | "update",
        "key": "记忆名称",
        "value": "记忆值" (可选),
        "persistent": True | False (可选，默认 False)
    }
    """
    action = action_data.get("action")
    key = action_data.get("key")
    value = action_data.get("value")
    persistent = action_data.get("persistent", False)

    if not action or not key:
        return {"status": "error", "message": "Missing 'action' or 'key'."}

    try:
        if action == "save":
            _manager.remember(key, value, persistent)
            return {"status": "success", "message": f"Saved key '{key}'."}

        elif action == "query":
            result = _manager.recall(key, persistent)
            return {"status": "success", "data": result}

        elif action == "delete":
            success = _manager.forget(key, persistent)
            return {"status": "success" if success else "failed", "message": f"Deleted key '{key}': {success}"}

        elif action == "update":
            success = _manager.modify(key, value, persistent)
            return {"status": "success" if success else "failed", "message": f"Updated key '{key}': {success}"}

        else:
            return {"status": "error", "message": f"Unknown action: {action}"}
            
    except Exception as e:
        return {"status": "error", "message": str(e)}# Memory module
