"""
通用转换处理器
提供常见的文本转换功能
"""

import re
from .base import TextProcessor


class CommonConverter(TextProcessor):
    """通用转换处理器"""
    
    def __init__(self):
        super().__init__(
            name="通用转换",
            description="提供括号转换、单词首字母大写等常见转换功能"
        )
        # 定义括号映射关系
        self.bracket_mapping = {
            '(': '（',
            ')': '）'
        }
    
    def convert_brackets(self, text: str) -> str:
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
    
    def capitalize_words(self, text: str) -> str:
        """
        将文本中所有英文单词的首字母大写
        
        Args:
            text: 输入的文本
            
        Returns:
            转换后的文本
        """
        return text.title()
    
    def process(self, text: str) -> str:
        """
        默认处理方法（暂不使用）
        
        Args:
            text: 输入的文本
            
        Returns:
            原文本
        """
        return text
    
    def process_with_arg(self, text: str, arg: str) -> str:
        """
        根据参数处理文本
        
        Args:
            text: 输入的文本
            arg: 操作参数
            
        Returns:
            处理后的文本
        """
        if arg == "convert_brackets_en_to_cn":
            return self.convert_brackets(text)
        elif arg == "capitalize_words":
            return self.capitalize_words(text)
        return text
    
    def get_menu_items(self, text: str = "") -> list:
        """获取菜单项"""
        return [
            {
                "title": "括号转换(EN→CN)",
                "subtitle": "将英文括号 () 转换为中文括号 （）",
                "arg": "convert_brackets_en_to_cn",
                "valid": True,
                "quicklookurl": self.convert_brackets(text)
            },
            {
                "title": "单词首字母大写",
                "subtitle": "将所有英文单词的首字母转换为大写",
                "arg": "capitalize_words",
                "valid": True,
                "quicklookurl": self.capitalize_words(text)
            }
        ]
