from modules.memory.short_memory import ShortMemory
from modules.memory.long_memory import LongMemory
from typing import Any, Optional

class MemoryManager:
    """
    记忆管理器，负责协调短期记忆与长期记忆。
    """
    def __init__(self) -> None:
        self.short_term: ShortMemory = ShortMemory()
        self.long_term: LongMemory = LongMemory()

    def remember(self, key: str, value: Any, persistent: bool = False) -> None:
        """
        保存一条记忆。
        
        :param key: 记忆键
        :param value: 记忆内容
        :param persistent: 是否属于需要持久化的长期记忆
        """
        if persistent:
            self.long_term.save(key, value)
        else:
            self.short_term.save(key, value)

    def recall(self, key: str, persistent: bool = False) -> Optional[Any]:
        """
        查询/检索一条记忆。
        """
        if persistent:
            return self.long_term.query(key)
        return self.short_term.query(key)

    def forget(self, key: str, persistent: bool = False) -> bool:
        """
        删除一条记忆。
        """
        if persistent:
            return self.long_term.delete(key)
        return self.short_term.delete(key)

    def modify(self, key: str, value: Any, persistent: bool = False) -> bool:
        """
        修改/更新一条记忆。
        """
        if persistent:
            return self.long_term.update(key, value)
        return self.short_term.update(key, value)
