"""
Markdown文本处理器
处理Markdown相关的文本转换
"""

import re
from .base import TextProcessor


class MarkdownProcessor(TextProcessor):
    """Markdown文本处理器"""
    
    def __init__(self):
        super().__init__(
            name="Markdown文本处理",
            description="处理Markdown相关的文本转换"
        )
    
    def convert_math_delimiters(self, text: str) -> str:
        """
        将LaTeX风格的数学公式界定符替换为美元符号风格
        
        Args:
            text: 包含LaTeX公式的输入字符串
            
        Returns:
            界定符被替换后的字符串
        """
        # 替换行内公式 \( ... \) 为 $ ... $
        text = re.sub(r'\\\((.*?)\\\)', r'$\1$', text)
        
        # 替换行间公式 \[ ... \] 为 $$ ... $$
        text = re.sub(r'\\\[(.*?)\\\]', r'$$\1$$', text)
        
        return text
    
    def process(self, text: str) -> str:
        """
        处理Markdown文本（默认转换数学公式界定符）
        
        Args:
            text: 输入的文本
            
        Returns:
            处理后的文本
        """
        return self.convert_math_delimiters(text)
    
    def process_with_arg(self, text: str, arg: str) -> str:
        """
        根据参数处理文本
        """
        if arg == "markdown-replace-math-indicator":
            return self.convert_math_delimiters(text)
        return text
    
    def get_menu_items(self, text: str = "") -> list:
        """获取菜单项"""
        return [
            {
                "title": "替换数学公式中的indicator",
                "subtitle": "将\\[ \\]替换为$$",
                "arg": "markdown-replace-math-indicator",
                "valid": True,
                "quicklookurl": self.convert_math_delimiters(text),
                "icon": "imgs/markdown.svg"
            }
        ] 