"""
括号转换处理器
将英文括号转换为中文括号
"""

import re
from .base import TextProcessor


class BracketConverter(TextProcessor):
    """括号转换处理器"""
    
    def __init__(self):
        super().__init__(
            name="括号转换(EN-CN)",
            description="将英文括号转换为中文括号"
        )
        # 定义括号映射关系
        self.bracket_mapping = {
            '(': '（',
            ')': '）'
        }
    
    def process(self, text: str) -> str:
        """
        将文本中的英文括号转换为中文括号
        
        Args:
            text: 输入的文本
            
        Returns:
            转换后的文本
        """
        converted_text = text
        for eng_bracket, ch_bracket in self.bracket_mapping.items():
            converted_text = converted_text.replace(eng_bracket, ch_bracket)
        
        return converted_text
    
    def process_with_arg(self, text: str, arg: str) -> str:
        """
        根据参数处理文本
        """
        if arg == "change_brackets(EN-CN)":
            return self.process(text)
        return text
    
    def get_menu_items(self, text: str = "") -> list:
        """获取菜单项"""
        return [{
            "title": self.name,
            "subtitle": self.description,
            "arg": "change_brackets(EN-CN)",
            "valid": True,
            "quicklookurl": self.process(text)
        }] 
        
        