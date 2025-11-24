"""
Mermaid代码处理器
处理Mermaid图表相关的文本转换
"""

import re
from .base import TextProcessor


class MermaidProcessor(TextProcessor):
    """Mermaid代码处理器"""
    
    def __init__(self):
        super().__init__(
            name="Mermaid代码处理",
            description="处理Mermaid图表相关的文本转换"
        )
    
    
    def add_quotes_to_nodes(self, text: str) -> str:
        """
        为Mermaid节点添加引号
        
        Args:
            text: 输入的文本
            
        Returns:
            处理后的文本
        """
        # 为节点加引号，匹配 [text] 模式并转换为 ["text"]
        pattern = r'(\[)([^\[\]]+)(\])'
        return re.sub(pattern, r'["\2"]', text)
    
    def process(self, text: str) -> str:
        """
        处理Mermaid代码（默认添加引号到节点）
        
        Args:
            text: 输入的文本
            
        Returns:
            处理后的文本
        """
        return self.add_quotes_to_nodes(text)
    
    
    def process_with_arg(self, text: str, arg: str) -> str:
        """
        根据参数处理文本
        """
        if arg == "mermaid-quote":
            return self.add_quotes_to_nodes(text)
        return text
    
    def get_menu_items(self, text: str = "") -> list:
        """获取菜单项"""
        return [
            {
                "title": '使用""将cell里的文字括起来',
                "arg": "mermaid-quote",
                "valid": True,
                "quicklookurl": self.add_quotes_to_nodes(text),
                "icon": "imgs/mermaid.png"
            }
        ] 