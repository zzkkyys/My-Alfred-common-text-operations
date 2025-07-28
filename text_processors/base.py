"""
文本处理器基类
定义所有文本处理器必须实现的接口
"""

from abc import ABC, abstractmethod
from typing import Dict, Any, Optional


class TextProcessor(ABC):
    """文本处理器基类"""
    
    def __init__(self, name: str, description: str = ""):
        self.name = name
        self.description = description
    
    @abstractmethod
    def process(self, text: str) -> str:
        """
        处理文本的核心方法
        
        Args:
            text: 输入的文本
            
        Returns:
            处理后的文本
        """
        pass
    
    @abstractmethod
    def get_menu_items(self, text: str = "") -> list:
        """
        获取菜单项列表
        
        Returns:
            包含菜单项信息的列表
        """
        pass
    
    def get_info(self) -> Dict[str, Any]:
        """
        获取处理器信息
        
        Returns:
            包含处理器信息的字典
        """
        return {
            "name": self.name,
            "description": self.description
        } 