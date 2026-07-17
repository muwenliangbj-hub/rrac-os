from typing import Dict, Any, Optional

class ShortMemory:
    """
    短期记忆管理类。数据保存在运行内存中，进程结束后失效。
    """
    def __init__(self) -> None:
        """初始化短期记忆存储字典。"""
        self._data: dict[str, Any] = {}

    def save(self, key: str, value: Any) -> None:
        """
        保存一条短期记忆。
        """
        self._data[key] = value

    def query(self, key: str) -> Optional[Any]:
        """
        查询一条短期记忆。
        """
        return self._data.get(key, None)

    def delete(self, key: str) -> bool:
        """
        删除一条短期记忆。
        """
        if key in self._data:
            del self._data[key]
            return True
        return False

    def update(self, key: str, value: Any) -> bool:
        """
        修改/更新一条短期记忆。
        """
        if key in self._data:
            self._data[key] = value
            return True
        return False
