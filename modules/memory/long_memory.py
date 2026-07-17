import os
import json
from typing import Dict, Any, Optional

class LongMemory:
    """
    长期记忆管理类。数据通过本地 JSON 文件进行持久化存储。
    """
    def __init__(self, storage_path: str = "long_term_storage.json") -> None:
        """
        :param storage_path: 长期记忆存储的本地文件路径
        """
        self.storage_path: str = storage_path
        self._data: dict[str, Any] = self._load_storage()

    def _load_storage(self) -> dict[str, Any]:
        """从本地加载长期记忆。"""
        if os.path.exists(self.storage_path):
            try:
                with open(self.storage_path, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                return {}
        return {}

    def _save_to_storage(self) -> None:
        """保存记忆到本地文件。"""
        try:
            with open(self.storage_path, "w", encoding="utf-8") as f:
                json.dump(self._data, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Error saving long term memory: {e}")

    def save(self, key: str, value: Any) -> None:
        """
        保存一条长期记忆并持久化。
        """
        self._data[key] = value
        self._save_to_storage()

    def query(self, key: str) -> Optional[Any]:
        """
        查询一条长期记忆。
        """
        return self._data.get(key, None)

    def delete(self, key: str) -> bool:
        """
        删除一条长期记忆。
        """
        if key in self._data:
            del self._data[key]
            self._save_to_storage()
            return True
        return False

    def update(self, key: str, value: Any) -> bool:
        """
        更新一条长期记忆。
        """
        if key in self._data:
            self._data[key] = value
            self._save_to_storage()
            return True
        return False
