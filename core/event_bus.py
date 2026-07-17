from typing import Callable, Dict, List, Any

class EventBus:
    """
    RRAC-OS 简单事件总线，负责组件间的解耦通信。
    """
    def __init__(self) -> None:
        """初始化订阅者存储结构。"""
        self._listeners: dict[str, list[Callable]] = {}

    def subscribe(self, event_type: str, callback: Callable) -> None:
        """
        订阅指定事件。
        
        :param event_type: 事件类型名称
        :param callback: 触发事件时的回调函数
        """
        if event_type not in self._listeners:
            self._listeners[event_type] = []
        self._listeners[event_type].append(callback)

    def unsubscribe(self, event_type: str, callback: Callable) -> None:
        """
        取消订阅指定事件。
        """
        if event_type in self._listeners and callback in self._listeners[event_type]:
            self._listeners[event_type].remove(callback)

    def publish(self, event_type: str, data: Any = None) -> None:
        """
        发布事件，通知所有订阅者。
        """
        if event_type in self._listeners:
            for callback in self._listeners[event_type]:
                callback(data)
