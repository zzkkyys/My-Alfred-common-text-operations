"""
数字格式化处理器
将数字按千位加逗号分隔符
"""

import re
from .base import TextProcessor


class NumberFormatter(TextProcessor):
    """数字格式化处理器"""
    
    def __init__(self):
        super().__init__(
            name="格式化千分数字",
            description="将数字按千位加逗号分隔符，如 1932131 转换为 1,932,131"
        )
    
    def process(self, text: str) -> str:
        """
        将数字按千位加逗号分隔符
        
        Args:
            text: 输入的文本
            
        Returns:
            格式化后的文本
        """
        def add_commas(match):
            number = match.group(0)
            # 处理小数
            if '.' in number:
                integer_part, decimal_part = number.split('.')
                # 从右往左每三位加一个逗号
                formatted_integer = ''
                for i in range(len(integer_part)):
                    if i > 0 and (len(integer_part) - i) % 3 == 0:
                        formatted_integer += ','
                    formatted_integer += integer_part[i]
                return f"{formatted_integer}.{decimal_part}"
            else:
                # 从右往左每三位加一个逗号
                formatted_number = ''
                for i in range(len(number)):
                    if i > 0 and (len(number) - i) % 3 == 0:
                        formatted_number += ','
                    formatted_number += number[i]
                return formatted_number
        
        # 匹配数字（包括小数）
        pattern = r'\b\d+(?:\.\d+)?\b'
        return re.sub(pattern, add_commas, text)
    
    def process_with_arg(self, text: str, arg: str) -> str:
        """
        根据参数处理文本
        """
        if arg == "format_thousand_separator":
            return self.process(text)
        return text
    
    def get_menu_items(self, text: str = "") -> list:
        """获取菜单项"""
        return [{
            "title": self.name,
            "subtitle": "convert 1932131 to 1,932,131",
            "arg": "format_thousand_separator",
            "valid": True,
            "quicklookurl": self.process(text)
        }] 
        
        
        